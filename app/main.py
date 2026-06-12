from fastapi import FastAPI
from . routers import course,user

app=FastAPI()

app.include_router(course.router)
app.include_router(user.router)












# ,HTTPException,status,Response,Depends
# from pydantic import BaseModel,HttpUrl
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time
# from . import models,schema,utils
# from sqlalchemy.orm import Session
# from .database import engine,get_db
# from typing import List

# app = FastAPI()

# models.base.metadata.create_all(bind=engine)

                                  ###  RAW SQL  

#defining request body schema
#POST is used to create new data

# while True:
#     try:
#         con= psycopg2.connect(host='localhost',database='firstday',user='postgres',password='1234',cursor_factory=RealDictCursor)
#         cursor=con.cursor()
#         print("successfully connected")
#         break
#     except Exception as error :
#         print("Connection Failed")
#         print("Error",error)
#         print("Retrying in 2 seconds...")
#         time.sleep(2)

# class course(BaseModel):
#     name: str
#     instructor: str
#     duration: float
#     website: HttpUrl
# @app.post("/post")
# def create_post(post:course):
#     cursor.execute("""INSERT INTO course(name,instructor,duration,website) VALUES (%s,%s,%s,%s)RETURNING *""",
#                    (post.name,post.instructor,post.duration,str(post.website)))
#     new_post=cursor.fetchone()
#     con.commit()


#     return{"data": new_post}

# @app.get("/")
# def firstday():
#     cursor.execute("SELECT * FROM course")
#     data=cursor.fetchall()
#     return {"Data": data}

# @app.get("/course/{id}")
# def get_course(id:int):
#     cursor.execute("select * from course where id=%s",(id,))
#     data=cursor.fetchone()
    
#     if not data :
#        raise HTTPException(
#         status_code = status.HTTP_404_NOT_FOUND,
#         detail=f"course with id {id} not found"
#     )
#     return{"Course Details": data}

# @app.delete("/course/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_course(id:int):
#     cursor.execute("delete from course where id=%s returning *",(id,))
#     delete_course=cursor.fetchone()
#     con.commit()
#     if not delete_course:
#         raise HTTPException(
#         status_code =status.HTTP_404_NOT_FOUND,
#         detail=f"course with id{id} not found"
#     )
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.put("/course/{id}")
# def update_course(id:int,post:course):
#     cursor.execute("""update course set name=%s,instructor=%s,duration=%s,website=%s where id=%s returning *""",
#                    (post.name,post.instructor,post.duration,str(post.website),id))
#     update_course=cursor.fetchone()
#     con.commit()
#     if not update_course:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"course with id {id} not found"
#         )
#     return{"UPDATED COURSE":update_course}












