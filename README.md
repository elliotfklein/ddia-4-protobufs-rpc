# DDIA Chapter 4: In the (proto)Buff

Install `grpcio-tools`:

```
pip install -r requirements.txt
```

Generate both RPC stubs + protobuf classes:

```
python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. ./post.proto
```

## Next Steps

1. Run `python server.py` and `python client.py` (in separate terminals) to create some posts — check out `posts.db` and/or `posts.json` to see the encoded data
2. Add comments (either as nested objects with `Post` or separate `Comment` type) + create/read RPCs
3. Some ideas for schema evolution (make sure to regenerate the protobuf classes after each change):

- Try changing `Post.id` from an `int32` to a `string` (what happens with old encoded `Post`s when the server deserializes them?)
- Mark `Post.id` as reserved, then add a new `string` `uuid` field instead
- Change `Post.views` to a `uint64`

4. Try a "rolling upgrade" for a backward-compatible change:

- Leave the server/client running
- Change the `Post` schema in `post.proto`
- Regenerate the protobuf classes
- Make code changes for the new fields
- Run the server/client again on a different port

### Old commands just for generating protobuf classes

**Just use above**

~~Install `protoc`:~~

~~`apt-get install protobuf-compiler`~~

~~Generate `post_pb2.py` from `post.proto`:~~

~~`protoc --python_out=. ./post.proto`~~
