import logging
from typing import Any, Dict
from fastapi import HTTPException

logger = logging.getLogger(__name__)

def handle_errors(func):
    """Decorator to handle common errors and logging"""
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {str(e)}")
            raise HTTPException(
                status_code=500,
                detail="Internal server error"
            )
    return wrapper

def validate_input(data: Dict[str, Any], required_fields: list) -> bool:
    """Validate input data against required fields"""
    missing_fields = [
        field for field in required_fields 
        if field not in data or data[field] is None
    ]
    
    if missing_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Missing required fields: {', '.join(missing_fields)}"
        )
    return True

def format_response(data: Any, status: str = "success") -> Dict[str, Any]:
    """Standardize API response format"""
    return {
        "status": status,
        "data": data
    }