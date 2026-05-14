from sqlalchemy import Column,Integer,String,Float
from .database import base


class courses(base):
    __tablename__ ="course"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    instructor=Column(String,nullable=False)
    duration=Column(Float,nullable=False)
    website=Column(String,nullable=False)
