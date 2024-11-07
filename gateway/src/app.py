from fastapi import FastAPI
from nameko_grpc import ServiceRpcProxy

from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="./resources/.env")

app = FastAPI()

STREAMING_SERVICE = "streaming.service.StreamingService"


@app.get("/unary-unary")
async def unary_unary():
    async with ServiceRpcProxy(STREAMING_SERVICE) as rpc:
        response = await rpc.unary_unary_method(request="Hello")
        return {"response": response}


@app.get("/unary-stream")
async def unary_stream():
    async with ServiceRpcProxy(STREAMING_SERVICE) as rpc:
        responses = await rpc.unary_stream_method(request="Hello")
        return {"responses": list(responses)}


@app.get("/stream-unary")
async def stream_unary():
    async with ServiceRpcProxy(STREAMING_SERVICE) as rpc:
        response = await rpc.stream_unary_method(request=["Hello", "World"])
        return {"response": response}


@app.get("/stream-stream")
async def stream_stream():
    async with ServiceRpcProxy(STREAMING_SERVICE) as rpc:
        responses = await rpc.stream_stream_method(request=["Hello", "World"])
        return {"responses": list(responses)}
