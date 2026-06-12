from sqlalchemy import Column,Integer,String,Float,TIMESTAMP,text
from .database import base


class courses(base):
    __tablename__ ="course"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    instructor=Column(String,nullable=False)
    duration=Column(Float,nullable=False)
    website=Column(String,nullable=False)

class user(base):
    __tablename__= "user"
    id = Column(Integer,primary_key=True,nullable=False)
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    
