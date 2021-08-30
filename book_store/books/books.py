# `app` is the package
# `books` is the package inside the 'app' package

from book_store.dependencies import pagination_params,sort_using_params
from fastapi import APIRouter
from fastapi.param_functions import Depends
from book_store.books.models import MyBook

from enum import Enum
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
    """ get data of book though payload"""
    return book


@router.get("")
def get_books(options:dict=Depends(pagination_params)
        ,sort_options:dict=Depends(sort_using_params)):
    return {"options":options}



