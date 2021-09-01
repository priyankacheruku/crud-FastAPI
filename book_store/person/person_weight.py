# here an example of arbitary router
from fastapi.applications import FastAPI
from book_store.dependencies import pagination_params
from fastapi import APIRouter
from typing import Dict
from fastapi.encoders import jsonable_encoder

from fastapi.param_functions import Body, Depends, Path

from book_store.person.models import Person, PersonResponse
from pymongo import MongoClient
from bson.objectid import ObjectId

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
        person_collection = client["book_store"]["person"]
        result = person_collection.insert_one(jsonable_encoder(person))
        return {"message":result.acknowledged}
    return {"message":"error"}

# persons = {
#     1: {
#         "name":"priyanka",
#         "identity":"developer",
#     },
#     2: {
#         "name":"xyz",
#         "identity":"developer",
#     }
# }

### using Path for adding validation fot path variable
@router.put("/person/{person_id}")
def update_person(*,person_id:str= Path(default=...,
                description="the primary key to identify person")
            ,person:Person
            ):
    # one way
    # person = person.__dict__

    # another way
    encoded_person = jsonable_encoder(person)
    with MongoClient() as client:
        person_collection = client["book_store"]["person"]
        x = person_collection.find_one({"_id":ObjectId(person_id)})
        if x:
            result = person_collection.update_one({"_id": ObjectId(person_id)},
                                         {"$set": encoded_person})
            if result.acknowledged:
                return True
            return False
        else:
            return{ "message":"not found"}
    return 
    

# using `Body` to differentiate `payload value` from `query parameter`
@router.post("/person/role/{person_id}")
def send_role_in_payload(*,person_id:int,
        role:str=Body(...),
        person:Person):
    return role

def convert_to_json(person):
    return {
        "id": str(person["_id"]),
        "name":person["name"],
        "identity":person["identity"]

    }

@router.get("/person")
def get_persons(options:dict=Depends(pagination_params)):
    with MongoClient() as client:
        person_collection = client["book_store"]["person"]
        persons = person_collection.find()
        results = []
        for person in persons:
            results.append(convert_to_json(person))
            
        return {"message":"using pagination params","options":options,"results":results}
    return False


@router.get("/person/{person_id}")
def get_person(person_id:str):
    with MongoClient() as client:
        person_collection = client["book_store"]["person"]
        
        person = convert_to_json(person_collection.find_one({"_id":ObjectId(person_id)}))
        return person


@router.delete("/person/{person_id}")
def delete_person(person_id:str):
    with MongoClient() as client:
        person_collection = client["book_store"]["person"]
        x = person_collection.delete_one({"_id":ObjectId(person_id)})
        if x:
            return True
        return False
