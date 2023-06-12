# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import image_pb2 as image__pb2


class image_tranferStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.send_me_image = channel.unary_stream(
                '/image.image_tranfer/send_me_image',
                request_serializer=image__pb2.image_request.SerializeToString,
                response_deserializer=image__pb2.image_response.FromString,
                )
        self.upload_image = channel.stream_unary(
                '/image.image_tranfer/upload_image',
                request_serializer=image__pb2.image_up.SerializeToString,
                response_deserializer=image__pb2.ack_response.FromString,
                )
        self.ack = channel.unary_unary(
                '/image.image_tranfer/ack',
                request_serializer=image__pb2.ack_request.SerializeToString,
                response_deserializer=image__pb2.ack_response.FromString,
                )
        self.are_you_ready = channel.unary_unary(
                '/image.image_tranfer/are_you_ready',
                request_serializer=image__pb2.ready_request.SerializeToString,
                response_deserializer=image__pb2.ready_response.FromString,
                )


class image_tranferServicer(object):
    """Missing associated documentation comment in .proto file."""

    def send_me_image(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def upload_image(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ack(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def are_you_ready(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_image_tranferServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'send_me_image': grpc.unary_stream_rpc_method_handler(
                    servicer.send_me_image,
                    request_deserializer=image__pb2.image_request.FromString,
                    response_serializer=image__pb2.image_response.SerializeToString,
            ),
            'upload_image': grpc.stream_unary_rpc_method_handler(
                    servicer.upload_image,
                    request_deserializer=image__pb2.image_up.FromString,
                    response_serializer=image__pb2.ack_response.SerializeToString,
            ),
            'ack': grpc.unary_unary_rpc_method_handler(
                    servicer.ack,
                    request_deserializer=image__pb2.ack_request.FromString,
                    response_serializer=image__pb2.ack_response.SerializeToString,
            ),
            'are_you_ready': grpc.unary_unary_rpc_method_handler(
                    servicer.are_you_ready,
                    request_deserializer=image__pb2.ready_request.FromString,
                    response_serializer=image__pb2.ready_response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'image.image_tranfer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class image_tranfer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def send_me_image(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/image.image_tranfer/send_me_image',
            image__pb2.image_request.SerializeToString,
            image__pb2.image_response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def upload_image(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/image.image_tranfer/upload_image',
            image__pb2.image_up.SerializeToString,
            image__pb2.ack_response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ack(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/image.image_tranfer/ack',
            image__pb2.ack_request.SerializeToString,
            image__pb2.ack_response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def are_you_ready(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/image.image_tranfer/are_you_ready',
            image__pb2.ready_request.SerializeToString,
            image__pb2.ready_response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
