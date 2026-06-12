from fastapi import FastAPI,HTTPException,status,Response,Depends,APIRouter
from sqlalchemy.orm import Session
from .. import models,schema,utils
from .. database import get_db
from typing import List

router=APIRouter(
    prefix="/users",
    tags=["USERS"]
)

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schema.UserRes)
def create_user(user:schema.UserCreate,db:Session=Depends(get_db)):
    if db.query(models.user).filter(models.user.email==user.email).first():
        raise HTTPException(400,"Email already exists")
    hashed_password=utils.hash_password(user.password)
    user.password=hashed_password
    new_user=models.user(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user