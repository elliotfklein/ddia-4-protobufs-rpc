from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetPostByIdRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetPostsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Post(_message.Message):
    __slots__ = ["a_new_field", "author_id", "body", "id", "likes", "tags", "title"]
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    A_NEW_FIELD_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LIKES_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    a_new_field: bool
    author_id: str
    body: str
    id: int
    likes: int
    tags: _containers.RepeatedScalarFieldContainer[str]
    title: str
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., body: _Optional[str] = ..., author_id: _Optional[str] = ..., likes: _Optional[int] = ..., a_new_field: bool = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...

class PostDB(_message.Message):
    __slots__ = ["posts"]
    POSTS_FIELD_NUMBER: _ClassVar[int]
    posts: _containers.RepeatedCompositeFieldContainer[Post]
    def __init__(self, posts: _Optional[_Iterable[_Union[Post, _Mapping]]] = ...) -> None: ...
