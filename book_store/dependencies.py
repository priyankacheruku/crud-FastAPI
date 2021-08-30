from enum import Enum
from typing import Optional
from fastapi import Depends,APIRouter
from fastapi.param_functions import Header

async def verify_token(token:str=Header(...)):
    print("Oh no! validation missing")
    return {"token":token}

async def pagination_params(page_number:Optional[int]=1,page_size:Optional[int]=10):
    return {"page_number":page_number,"page_size":page_size}

async def search_content(search:Optional[str]=None):
    return {"search":search}

class Options(Enum):
    ascending ="ascending"
    descending = "descending"

async def  sort_using_params(sort_by:Optional[Options]=None,
        sort_by_field:Optional[str]=None):
    return {"sort_by":sort_by,"sort_by_field":sort_by_field}

def swagger_auth(token:Header(...)):
    return {"message":"ok"}