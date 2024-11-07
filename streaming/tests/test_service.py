import pytest
from src.service_pb2 import ExampleRequest


def test_unary_unary(grpc_client):
    """Test the Unary-Unary RPC method."""
    response = grpc_client.unary_unary(ExampleRequest(value="Hello"))
    assert response.message == "Unary-Unary response to 'Hello'"


def test_unary_stream(grpc_client):
    """Test the Unary-Stream RPC method."""
    responses = list(grpc_client.unary_stream(ExampleRequest(value="Hello")))
    assert responses == ["Stream part 1 for 'Hello'", "Stream part 2 for 'Hello'"]


def test_stream_unary(grpc_client):
    """Test the Stream-Unary RPC method."""
    response = grpc_client.stream_unary(
        [ExampleRequest(value="Hello"), ExampleRequest(value="World")]
    )
    assert response == "Stream-Unary response to 'Hello World'"


def test_stream_stream(grpc_client):
    """Test the Stream-Stream RPC method."""
    responses = list(
        grpc_client.stream_stream(ExampleRequest(value=["Hello", "World"]))
    )
    assert responses == ["Stream part for 'Hello'", "Stream part for 'World'"]
