from pydantic.fields import Field
from pydantic.main import BaseModel


class Person(BaseModel):
    name:str
    identity: str = Field(None,max_length=20)