import post_pb2
import post_pb2_grpc
import grpc
import os
from google.protobuf import json_format
from concurrent import futures

DB_FILENAME = os.path.join(os.getcwd(), "posts.db")
JSON_FILENAME = os.path.join(os.getcwd(), "posts.json")

posts = post_pb2.PostDB()
if os.path.exists(DB_FILENAME):
    with open(DB_FILENAME, "rb") as f:
        posts.ParseFromString(f.read())

print(f"Server found {len(posts.posts)} posts:")
print(posts)


class PostsServiceServicer(post_pb2_grpc.PostsServiceServicer):
    def GetPosts(self, _request, _context):
        return posts

    def GetPostById(self, request, _context):
        for post in posts.posts:
            if post.id == request.id:
                return post
        raise grpc.RpcError(grpc.StatusCode.NOT_FOUND)

    def CreatePost(self, request, _context):
        assert request.id == 0
        request.id = len(posts.posts)
        posts.posts.append(request)

        print("Created post:")
        print(posts.posts[-1])
        compare_encoding_size(posts.posts[-1])

        with open(DB_FILENAME, "wb") as f:
            f.write(posts.SerializeToString())
        with open(JSON_FILENAME, "w") as f:
            f.write(json_format.MessageToJson(posts))

        return posts.posts[-1]


def compare_encoding_size(post: post_pb2.Post):
    post_bytes = post.SerializeToString()
    post_json = json_format.MessageToJson(post)
    print(f"Protobuf size: {len(post_bytes)} bytes")
    print(f"JSON size: {len(post_json)} bytes")
    print(
        f"JSON is {len(post_json) / len(post_bytes):.2f}x larger than protobuf"
    )


if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    post_pb2_grpc.add_PostsServiceServicer_to_server(
        PostsServiceServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()  # Non-blocking
    server.wait_for_termination()
