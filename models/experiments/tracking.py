import logging
from datetime import datetime
from typing import Dict, Any
import mlflow
from config.settings import settings

logger = logging.getLogger(__name__)

class ExperimentTracker:
    def __init__(self):
        self.experiment_name = "ai-platform"
        self.tracking_uri = "http://localhost:5000"
        mlflow.set_tracking_uri(self.tracking_uri)
        mlflow.set_experiment(self.experiment_name)

    def start_run(self, run_name: str = None):
        """Start a new experiment run"""
        if run_name is None:
            run_name = f"run-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        mlflow.start_run(run_name=run_name)
        logger.info(f"Started experiment run: {run_name}")

    def log_params(self, params: Dict[str, Any]):
        """Log experiment parameters"""
        mlflow.log_params(params)
        logger.info(f"Logged parameters: {params}")

    def log_metrics(self, metrics: Dict[str, Any]):
        """Log experiment metrics"""
        mlflow.log_metrics(metrics)
        logger.info(f"Logged metrics: {metrics}")

    def log_model(self, model, artifact_path: str):
        """Log a trained model"""
        mlflow.sklearn.log_model(model, artifact_path)
        logger.info(f"Logged model at: {artifact_path}")

    def end_run(self):
        """End the current experiment run"""
        mlflow.end_run()
        logger.info("Ended experiment run")