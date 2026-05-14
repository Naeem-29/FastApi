from fastapi import FastAPI,HTTPException,status,Response,Depends
from pydantic import BaseModel,HttpUrl
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models
from sqlalchemy.orm import Session
from .database import engine,get_db


app = FastAPI()

models.base.metadata.create_all(bind=engine)

#defining request body schema
#POST is used to create new data

class course(BaseModel):
    name: str
    instructor: str
    duration: float
    website: HttpUrl


while True:
    try:
        con= psycopg2.connect(host='localhost',database='firstday',user='postgres',password='1234',cursor_factory=RealDictCursor)
        cursor=con.cursor()
        print("successfully connected")
        break
    except Exception as error :
        print("Connection Failed")
        print("Error",error)
        print("Retrying in 2 seconds...")
        time.sleep(2)




@app.post("/post")
def create_post(post:course):
    cursor.execute("""INSERT INTO course(name,instructor,duration,website) VALUES (%s,%s,%s,%s)RETURNING *""",
                   (post.name,post.instructor,post.duration,str(post.website)))
    new_post=cursor.fetchone()
    con.commit()


    return{"data": new_post}

@app.post("/courses")
def create_course(course:course,db:Session=Depends(get_db)):
    new_cor=models.courses(
        name=course.name,
        instructor=course.instructor,
        duration=course.duration,
        website=str(course.website)
    )
    db.add(new_cor)
    db.commit()
    db.refresh(new_cor)
    return{"DATA":new_cor}


@app.get("/")
def firstday():
    cursor.execute("SELECT * FROM course")
    data=cursor.fetchall()
    return {"Data": data}



@app.get("/course/{id}")
def get_course(id:int):
    cursor.execute("select * from course where id=%s",(id,))
    data=cursor.fetchone()
    
    if not data :
       raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail=f"course with id {id} not found"
    )
    return{"Course Details": data}

@app.get("/coursealchemy/{id}")
def new_course(id:int,db:Session=Depends(get_db)):
    course=db.query(models.courses).filter(models.courses.id==id).first()
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"course with id {id} not found"
        )
    return{"course": course}

@app.delete("/course/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_course(id:int):
    cursor.execute("delete from course where id=%s returning *",(id,))
    delete_course=cursor.fetchone()
    con.commit()
    if not delete_course:
        raise HTTPException(
        status_code =status.HTTP_404_NOT_FOUND,
        detail=f"course with id{id} not found"
    )
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.delete("/course_delete/{id}",status_code=status.HTTP_204_NO_CONTENT)
def deleted(id:int,db:Session=Depends(get_db)):
    course_query=db.query(models.courses).filter(models.courses.id==id)
    delete_course=course_query.first()
    if not delete_course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"course with id {id} not found"
        )
    course_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/course/{id}")
def update_course(id:int,post:course):
    cursor.execute("""update course set name=%s,instructor=%s,duration=%s,website=%s where id=%s returning *""",
                   (post.name,post.instructor,post.duration,str(post.website),id))
    update_course=cursor.fetchone()
    con.commit()
    if not update_course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"course with id {id} not found"
        )
    return{"UPDATED COURSE":update_course}

@app.put("/newcourses/{id}")
def updatedNewCourse(id:int,course:course,db:Session=Depends(get_db)):
    course_query=db.query(models.courses).filter(models.courses.id==id)
    updated_course=course_query.first()
    if not updated_course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"course with id {id} not found"
        )
    updated_data=course.model_dump()
    updated_data["website"]=str(updated_data["website"])
    course_query.update(updated_data,synchronize_session=False)
    db.commit()
    db.refresh(updated_course)
    return{"updated_course":updated_course}


@app.get("/coursealchemy")
def course(db:Session=Depends(get_db)):
    course = db.query(models.courses).all()

    return {"course": course}
