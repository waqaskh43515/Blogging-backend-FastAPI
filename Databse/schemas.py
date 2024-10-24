from pydantic import BaseModel
from typing import List,Optional


class Blog1(BaseModel):
    title: str
    body: str
    class Confiq():
        orm_mode = True



class users(BaseModel):
    name: str
    email: str
    password: str
       
class showuser(BaseModel):
    name: str
    email: str
    blog: List[Blog1] = []
    class Confiq():
        orm_mode = True

class show_Blog(BaseModel):
    title: str
    body: str
    creator: showuser
    class Confiq():
        orm_mode = True


class login(BaseModel):
    username: str
    password: str   



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str]  = None         