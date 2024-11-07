# Streaming over AMQP using grpc

# Nameko Streams Boilerplate

This project serves as a boilerplate for Nameko streams, featuring a FastAPI gateway and a Nameko-based streaming service. It demonstrates four request-response patterns with support for asynchronous calls.

## Folder Structure

├── gateway
│ ├── src
│ │ └── app.py # FastAPI Application
│ ├── tests
│ │ └── test_app.py # Pytest Tests
│ ├── requirements.txt # Gateway Dependencies
│ └── resources
│ └── .env # Gateway Environment Variables
├── streaming
│ ├── src
│ │ └── service.py # Nameko Streaming Service
│ ├── requirements.txt # Streaming Dependencies
│ └── resources
│ └── .env # Streaming Environment Variables
└── README.md


## Services

### Gateway Service
- **Framework**: FastAPI
- **Path**: `gateway/src/app.py`
- **Description**: Acts as a gateway to consume the streaming service via gRPC, implementing four request-response patterns:
  - Unary-Unary
  - Unary-Stream
  - Stream-Unary
  - Stream-Stream

### Streaming Service
- **Framework**: Nameko with gRPC
- **Path**: `streaming/src/service.py`
- **Description**: Provides streaming capabilities with methods corresponding to each request-response pattern.

## Testing
- **Framework**: Pytest
- **Path**: `gateway/tests`
- **Description**: Contains tests for all four request-response patterns.

## Environment Variables
Both services use environment variables defined in their respective `resources/.env` files. Ensure to configure them as needed.
