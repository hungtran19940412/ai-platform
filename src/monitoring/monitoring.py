from prometheus_client import start_http_server, Counter, Histogram
import logging
from fastapi import Request
from typing import Callable
from fastapi.routing import APIRoute

logger = logging.getLogger(__name__)

# Prometheus metrics
REQUEST_COUNT = Counter(
    'api_requests_total',
    'Total number of API requests',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'api_request_latency_seconds',
    'API request latency in seconds',
    ['method', 'endpoint']
)

ERROR_COUNT = Counter(
    'api_errors_total',
    'Total number of API errors',
    ['method', 'endpoint', 'error_type']
)

class MonitoringRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request):
            with REQUEST_LATENCY.labels(
                method=request.method,
                endpoint=request.url.path
            ).time():
                try:
                    response = await original_route_handler(request)
                    REQUEST_COUNT.labels(
                        method=request.method,
                        endpoint=request.url.path,
                        status=response.status_code
                    ).inc()
                    return response
                except Exception as e:
                    ERROR_COUNT.labels(
                        method=request.method,
                        endpoint=request.url.path,
                        error_type=type(e).__name__
                    ).inc()
                    raise

        return custom_route_handler

def setup_monitoring():
    """Start Prometheus metrics server"""
    start_http_server(9090)
    logger.info("Monitoring server started on port 9090")