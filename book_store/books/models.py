from pydantic import BaseModel
from typing import Dict, Optional, Set, List
from pydantic.fields import Field

class Image(BaseModel):
    url :str
    name : str

class Comment(BaseModel):
    person_name: str
    comment: str

class MyBook(BaseModel):
    name : str
    author : str
    description : Optional[str] = Field(...,description="description of book")
    price : float
    tax : Optional[float] = None
    categories : Set[str] = set() # only unique values
    image : Optional[Image]=None # one image
    # image : Optional[List[Image]]=None # multiple images as optional
    comments: Optional[List[Comment]]

    class Config:
        """will be shown as a example"""
        schema_extra = {
            "example":{
                "name":"my new book",
                "author" :"priyanka",
                "description" :"its not a biopic",
                "price":0,
                "tax":100,
                "categories":["suspence","thriller"],
                "image":{
                    "url":"google.com/images/my_new_book",
                    "name":"coverpage"
                },
                "comments":[
                    {
                        "person_name":"YouKnow",
                        "comment":"one time read"
                    }

                ]

            }
        }

