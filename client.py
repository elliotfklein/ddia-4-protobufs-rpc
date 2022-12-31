import grpc
import post_pb2
import post_pb2_grpc


channel = grpc.insecure_channel("localhost:50051")
stub = post_pb2_grpc.PostsServiceStub(channel)

while True:
    command = input("Enter command (create/read/list): ")
    if command == "create":
        new_post = post_pb2.Post(
            id=None,
            title=input("Enter title: "),
            body=input("Enter body: "),
            author_id=input("Enter author ID: "),
            likes=None,
            tags=[
                tag.strip()
                for tag in input("Enter tags (comma-separated): ").split(",")
            ],
        )
        response = stub.CreatePost(new_post)
        print(f"Created post with ID: {response.id}")
    elif command == "read":
        post_id = int(input("Enter post ID: "))
        response = stub.GetPostById(post_pb2.GetPostByIdRequest(id=post_id))
        print(response)
    elif command == "list":
        response = stub.GetPosts(post_pb2.GetPostsRequest())
        print(f"Found {len(response.posts)} posts:")
        for post in response.posts:
            print(post)
    else:
        print("Invalid command")
