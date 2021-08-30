# one file structure 
from fastapi import FastAPI
from typing import Optional


app = FastAPI()

@app.get('/')
def home():
    """for baseurl"""
    return {"message":"welcome to the store"}

@app.get("/learn/{value}")
def path_parameter(value:int):
    return {"message":"Path parameter passed is: "+str(value)}

@app.get("/learn")
def query_parameter(x:str,value:Optional[str]=None):
    message = "Mandatory parameter is: " +x+" "
    if value:
        return {"message":message+"Query parameter passed is: "+str(value)}
    return {"message":message+"Optional query parameter not passed"}
