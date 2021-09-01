from typing import Optional
from pydantic.fields import Field
from pydantic import BaseModel,EmailStr


class Person(BaseModel):
    name:str
    identity: str = Field(None,max_length=20)

class PersonResponse(BaseModel):
    _id :str
    name:str
    identity: str

class UserIn(BaseModel):
    user_name : str
    password : str
    email : EmailStr
    full_name : Optional[str] = None

class UserOut(BaseModel):
    """for response model"""
    user_name :str
    email : EmailStr
    full_name : Optional[str]=None

    