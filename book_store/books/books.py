# `app` is the package
# `books` is the package inside the 'app' package

from bson.objectid import ObjectId
from fastapi.encoders import jsonable_encoder
from book_store.dependencies import pagination_params,sort_using_params
from fastapi import APIRouter
from fastapi.param_functions import Depends
from book_store.books.models import Comment, MyBook
from pymongo import MongoClient
from enum import Enum

client = MongoClient()
db = client["book_store"]
books_collection = db["books"]

def convert_book_to_json(book):
    book["_id"] = str(book["_id"])
    return book

class choices(str,Enum):
    shiv = "shiv"
    sita = "sita"

# router for the file 
router = APIRouter(prefix="/book",
                responses={404:{"descripion":"book not found"}})

@router.post("/choice")
def select_book(book:choices):
    """get choice through query parameter """
    return{"choice selected is "+ book.value}

@router.post("/")
def add_book(book:MyBook):
    """ post data of book though payload"""
    object = books_collection.insert_one(jsonable_encoder(book))
    if object.acknowledged:
        return True
    else:
        return False


@router.get("")
def get_books(options:dict=Depends(pagination_params)
        ,sort_options:dict=Depends(sort_using_params)):
    results = []
    for book in books_collection.find():
        results.append(convert_book_to_json(book))
    return {"results":results}

@router.put("/{book_id}")
def update_book(book_id:str,book:MyBook):
    """ get data of book though payload"""
    response = books_collection.update_one({"_id":ObjectId(book_id)},{"$set":jsonable_encoder(book)})
    if response.acknowledged:
        return convert_book_to_json(books_collection.find_one({"_id":ObjectId(book_id)}))
    else:
        return {"message":"error"}

@router.delete("/{book_id}")
def delete_book(book_id:str):
    object = books_collection.delete_one({"_id":ObjectId(book_id)})
    if object.deleted_count:
        return True
    else:
        return False



@router.get("/{book_id}")
def get_book(book_id:str):
    """ get data of book though payload"""
    return convert_book_to_json(books_collection.find_one({"_id":ObjectId(book_id)}))


@router.put("/comment/{book_id}")
def add_comment(book_id:str,comment:Comment):
    response = books_collection.update_one({"_id":ObjectId(book_id)},{"$push":{"comments":jsonable_encoder(comment)}})
    if response.acknowledged:
        return True

@router.delete("/comment/{book_id}")
def delete_comment(book_id:str,comment:Comment):
    response = books_collection.update_one({"_id":ObjectId(book_id)},{"$pull":{"comments":jsonable_encoder(comment)}})
    if response.acknowledged:
        return True

