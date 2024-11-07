import pytest
from src.service_pb2 import ExampleRequest


def test_unary_unary(grpc_client):
    """Test the Unary-Unary RPC method."""
    response = grpc_client.unary_unary(ExampleRequest(value="Hello"))
    assert response.message == "Unary-Unary response to 'Hello'"


def test_unary_stream(grpc_client):
    print("""Test the Unary-Stream RPC method.""")
    responses = grpc_client.unary_stream(ExampleRequest(value="Hello"))
    r = []
    for response in responses:
        r.append(response.message)
        assert response.message == "Hello"
    assert r == ["Hello", "Hello"]


def test_stream_unary(grpc_client):
    """Test the Stream-Unary RPC method."""
    response = grpc_client.stream_unary(
        [ExampleRequest(value="Hello"), ExampleRequest(value="World")]
    )
    assert response.message == "Hello,World"


def test_stream_stream(grpc_client):
    """Test the Stream-Stream RPC method."""
    responses = list(
        grpc_client.stream_stream(
            [ExampleRequest(value="Hello"), ExampleRequest(value="World")]
        )
    )
    assert [response.message for response in responses] == ["Hello", "World"]
