from pydantic import BaseModel,HttpUrl,EmailStr
from datetime import datetime

class Create_course(BaseModel):
    name: str
    instructor: str
    duration: float
    website: HttpUrl

class course_response(Create_course):
    id: int
    class Config:
        orm_model = True

# class User(BaseModel):
#     name: str
#     instructor: str

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserRes(BaseModel):
    id : int
    email : EmailStr
    created_at : datetime
    class config:
        orm_medel = True