import os, sys
import pytest
from dotenv import load_dotenv


print(f'Load .env: {load_dotenv(dotenv_path="./resources/.env")}', flush=True)
os.environ["ENVIRONMENT"] = "test"
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nameko_grpc.client import Client
from src.service_pb2_grpc import exampleStub


@pytest.fixture
def grpc_client():
    with Client("//127.0.0.1", exampleStub) as client:
        yield client
