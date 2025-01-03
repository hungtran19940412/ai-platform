import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    # API Configuration
    API_TITLE: str = "AI Platform API"
    API_VERSION: str = "1.0.0"
    API_DESCRIPTION: str = "API for AI-powered recommendation and insights platform"
    API_PREFIX: str = "/api/v1"
    
    # Database Configuration
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "ai_platform"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    
    # Redis Configuration
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    
    # Kafka Configuration
    KAFKA_BROKER: str = "localhost:9092"
    KAFKA_TOPIC_RECOMMENDATIONS: str = "recommendations"
    KAFKA_TOPIC_FINANCIAL: str = "financial"
    KAFKA_TOPIC_SUPPORT: str = "support"
    
    # Model Configuration
    MODEL_CACHE_SIZE: int = 1000
    MODEL_UPDATE_INTERVAL: int = 3600  # in seconds
    
    # Security Configuration
    JWT_SECRET_KEY: str = "secret-key"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 30
    
    # Monitoring Configuration
    PROMETHEUS_PORT: int = 9090
    GRAFANA_PORT: int = 3000
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()