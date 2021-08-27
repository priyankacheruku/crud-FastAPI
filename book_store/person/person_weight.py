# here an example of arbitary router
from fastapi import APIRouter
from typing import Dict

from fastapi.param_functions import Body, Path

from book_store.person.models import Person

router = APIRouter()

@router.post("/person-weight")
def add_weight(weight:Dict[int,float]):
    """accepts key as integer"""
    return weight


# to perform operations on person
@router.post("/person/")
def add_person(person:Person):
    return person

### using Path for adding validation fot path variable
@router.put("/person/{person_id}")
def add_person(*,person_id:int= Path(default=...,ge=0,le=100,
                description="the primary key to identify person")
            ,person:Person
            ):
    person = person.__dict__
    person.update({"id":person_id})
    return person

# using `Body` to differentiate `payload value` from `query parameter`
@router.post("/person/role/{person_id}")
def send_role_in_payload(*,person_id:int,
        role:str=Body(...),
        person:Person):
    return role


