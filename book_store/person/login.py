from fastapi import APIRouter
from fastapi.param_functions import Body, Form, Header

login_router = APIRouter()

@login_router.post("/login")
def login(user_name:str=Form(...),password:str=Form(...)):
    token = "your-token-"+user_name
    return {"message":"you loggined in as "+user_name,"token":token}
