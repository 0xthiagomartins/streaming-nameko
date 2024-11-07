from nameko.rpc import rpc
from nameko_grpc import GrpcService


class StreamingService(GrpcService):
    name = "streaming"

    @rpc
    def unary_unary_method(self, request):
        """
        Unary-Unary RPC:
        - Receives a single request and returns a single response.
        - This is the simplest form of RPC where both the client and server exchange one message each.
        """
        return f"Unary-Unary response to '{request}'"

    @rpc
    def unary_stream_method(self, request):
        """
        Unary-Stream RPC:
        - Receives a single request and returns a stream of responses.
        - Useful when the server needs to send multiple pieces of data in response to a single client request.
        """
        for msg in [f"Stream part 1 for '{request}'", f"Stream part 2 for '{request}'"]:
            yield msg

    @rpc
    def stream_unary_method(self, request):
        """
        Stream-Unary RPC:
        - Receives a stream of requests and returns a single response.
        - Ideal for scenarios where the client sends multiple messages to the server and expects a single consolidated response.
        """
        combined = " ".join(request)
        return f"Stream-Unary response to '{combined}'"

    @rpc
    def stream_stream_method(self, request):
        """
        Stream-Stream RPC:
        - Both the client and server exchange streams of messages.
        - Allows for continuous two-way communication between client and server.
        """
        for msg in request:
            yield f"Stream part for '{msg}'"
