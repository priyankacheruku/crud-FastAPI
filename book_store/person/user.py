from fastapi import APIRouter,File
from fastapi.datastructures import UploadFile
from book_store.person.models import UserIn,UserOut
from fastapi import status
router = APIRouter()


@router.post("/user",response_model=UserOut,response_model_exclude_unset=True)
def user_add(user:UserIn):
    """ to maintain different responses for the data"""
    return user

@router.get("/user",status_code=status.HTTP_200_OK)
def get_info():
    return({"message":"i used status from FastAPI"})

@router.post("/user/profile-photo")
def upload_profile_photo(image:UploadFile = File(...)):
    return {"image":image.filename}

