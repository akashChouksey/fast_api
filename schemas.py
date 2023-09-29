from pydantic import BaseModel
from typing import Optional, List, Union


class Blog(BaseModel):
    title: str
    body: str
    owner_id: int


class BlogTest(Blog):
    #owner_id: int
    class Config():
        from_attributes = True


class Test_User(BaseModel):
    name: str
    email: str

    class Config():
        from_attributes = True


class ShowBlogs(Blog):
    owner: Test_User

    class Config():
        from_attributes = True


class CreateUser(BaseModel):
    name: str
    email: str
    password: str
    #blog: List[ShowBlogs]


class User(BaseModel):
    name: str
    email: str
    items: List[Blog] = []

    class Config():
        from_attributes = True


class ShowAllBlogs(BaseModel):
    title: str
    body: str
    id: int
    owner: List[User] = []


class Login(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None



