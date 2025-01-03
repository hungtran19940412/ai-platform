import pytest
from fastapi.testclient import TestClient
from src.api.main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_recommendations_endpoint(client):
    test_data = {
        "user_id": "test_user",
        "context": {"preferences": ["tech", "books"]}
    }
    response = client.post("/api/v1/recommendations", json=test_data)
    assert response.status_code == 200
    assert "recommendations" in response.json()

def test_financial_analysis_endpoint(client):
    test_data = {
        "query": "What is the current price of AAPL?",
        "parameters": {}
    }
    response = client.post("/api/v1/financial/analyze", json=test_data)
    assert response.status_code == 200
    assert "insights" in response.json()

def test_support_query_endpoint(client):
    test_data = {
        "question": "How do I reset my password?",
        "language": "en"
    }
    response = client.post("/api/v1/support/query", json=test_data)
    assert response.status_code == 200
    assert "response" in response.json()