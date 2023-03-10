# DDIA Chapter 4: In the (proto)Buff

Install `grpcio-tools`:

```
pip install -r requirements.txt
```

Generate both RPC stubs + protobuf classes:

```
python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. ./post.proto
```

## Docker setup

1. Install Dev Containers VS Code extension: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers
2. Build the image: `docker build -t ddia-4 .`
3. Run the image: `docker run -it ddia-4`
4. Click the "remote" icon in the bottom left of VS Code, then select "Attach to Running Container" and select the `ddia-4` container you just ran

## Next Steps

1. Run `python server.py` and `python client.py` (in separate terminals) to create some posts — check out `posts.db` and/or `posts.json` to see the encoded data
2. Add comments (either as nested objects with `Post` or separate `Comment` type) + create/read RPCs
3. Some ideas for schema evolution (make sure to regenerate the protobuf classes after each change):

- Try changing `Post.id` from an `int32` to a `string` (what happens with old encoded `Post`s when the server deserializes them?)
- Mark `Post.id` as reserved, then add a new `string` `uuid` field instead
- Change `Post.views` to a `uint64`
- Relevant docs for [updating](https://developers.google.com/protocol-buffers/docs/proto3#updating) and [`reserved`](https://developers.google.com/protocol-buffers/docs/proto3#reserved)

4. Try a "rolling upgrade" for a backward-compatible change:

- Leave the server/client running
- Change the `Post` schema in `post.proto`
- Regenerate the protobuf classes
- Make code changes for the new fields
- Run the server/client again on a different port

## References

- https://grpc.io/docs/languages/python/basics/
- https://developers.google.com/protocol-buffers/docs/pythontutorial
- https://developers.google.com/protocol-buffers/docs/proto3

### Old commands just for generating protobuf classes

**Just use above**

~~Install `protoc`:~~

~~`apt-get install protobuf-compiler`~~

~~Generate `post_pb2.py` from `post.proto`:~~

~~`protoc --python_out=. ./post.proto`~~
