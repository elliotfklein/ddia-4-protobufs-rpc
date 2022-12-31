# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import post_pb2 as post__pb2


class PostsServiceStub(object):
    """CRUD for Posts 
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetPosts = channel.unary_unary(
                '/ddia.chapter4.PostsService/GetPosts',
                request_serializer=post__pb2.GetPostsRequest.SerializeToString,
                response_deserializer=post__pb2.PostDB.FromString,
                )
        self.GetPostById = channel.unary_unary(
                '/ddia.chapter4.PostsService/GetPostById',
                request_serializer=post__pb2.GetPostByIdRequest.SerializeToString,
                response_deserializer=post__pb2.Post.FromString,
                )
        self.CreatePost = channel.unary_unary(
                '/ddia.chapter4.PostsService/CreatePost',
                request_serializer=post__pb2.Post.SerializeToString,
                response_deserializer=post__pb2.Post.FromString,
                )


class PostsServiceServicer(object):
    """CRUD for Posts 
    """

    def GetPosts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPostById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreatePost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PostsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetPosts': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPosts,
                    request_deserializer=post__pb2.GetPostsRequest.FromString,
                    response_serializer=post__pb2.PostDB.SerializeToString,
            ),
            'GetPostById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPostById,
                    request_deserializer=post__pb2.GetPostByIdRequest.FromString,
                    response_serializer=post__pb2.Post.SerializeToString,
            ),
            'CreatePost': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePost,
                    request_deserializer=post__pb2.Post.FromString,
                    response_serializer=post__pb2.Post.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ddia.chapter4.PostsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PostsService(object):
    """CRUD for Posts 
    """

    @staticmethod
    def GetPosts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ddia.chapter4.PostsService/GetPosts',
            post__pb2.GetPostsRequest.SerializeToString,
            post__pb2.PostDB.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPostById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ddia.chapter4.PostsService/GetPostById',
            post__pb2.GetPostByIdRequest.SerializeToString,
            post__pb2.Post.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreatePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ddia.chapter4.PostsService/CreatePost',
            post__pb2.Post.SerializeToString,
            post__pb2.Post.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)