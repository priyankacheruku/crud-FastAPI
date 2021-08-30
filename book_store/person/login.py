from fastapi import APIRouter
from fastapi.param_functions import Form

login_router = APIRouter()

@login_router.post("/login")
def login(user_name:str=Form(...),password:str=Form(...)):
    return {"message":"you loggined in as "+user_name}