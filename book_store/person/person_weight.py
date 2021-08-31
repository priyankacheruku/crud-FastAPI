# here an example of arbitary router
from book_store.dependencies import pagination_params
from fastapi import APIRouter
from typing import Dict
from fastapi.encoders import jsonable_encoder

from fastapi.param_functions import Body, Depends, Path

from book_store.person.models import Person
from pymongo import MongoClient

router = APIRouter()

@router.post("/person-weight")
def add_weight(weight:Dict[int,float]):
    """accepts key as integer"""
    return weight


# to perform operations on person
@router.post("/person/")
def add_person(person:Person):
    jsonable_encoder(person)
    with MongoClient() as client:
        msg_collection = client["book_store"]["person"]
        result = msg_collection.insert_one(jsonable_encoder(person))
        return {"message":result.acknowledged}
    return {"message":"error"}

persons = {
    1: {
        "name":"priyanka",
        "identity":"developer",
    },
    2: {
        "name":"xyz",
        "identity":"developer",
    }
}

### using Path for adding validation fot path variable
@router.put("/person/{person_id}")
async def add_person(*,person_id:int= Path(default=...,ge=0,le=100,
                description="the primary key to identify person")
            ,person:Person
            ):
    # one way
    # person = person.__dict__

    # another way
    encoded_person = jsonable_encoder(person)
    persons[person_id] = encoded_person
    return encoded_person
    

# using `Body` to differentiate `payload value` from `query parameter`
@router.post("/person/role/{person_id}")
def send_role_in_payload(*,person_id:int,
        role:str=Body(...),
        person:Person):
    return role


@router.get("/person")
def get_persons(options:dict=Depends(pagination_params)):
    return {"message":"using pagination params","options":options}