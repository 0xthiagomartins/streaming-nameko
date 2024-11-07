import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_unary_unary():
    response = client.get("/unary-unary")
    assert response.status_code == 200
    assert "response" in response.json()


def test_unary_stream():
    response = client.get("/unary-stream")
    assert response.status_code == 200
    assert "responses" in response.json()


def test_stream_unary():
    response = client.get("/stream-unary")
    assert response.status_code == 200
    assert "response" in response.json()


def test_stream_stream():
    response = client.get("/stream-stream")
    assert response.status_code == 200
    assert "responses" in response.json()
