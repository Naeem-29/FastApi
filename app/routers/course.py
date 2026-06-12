from fastapi import FastAPI,HTTPException,status,Response,Depends,APIRouter
from sqlalchemy.orm import Session
from .. import models,schema
from .. database import get_db
from typing import List

router=APIRouter(
    prefix="/course",
    tags=["courses"]
)


@router.post("/",response_model=schema.course_response,status_code=status.HTTP_201_CREATED)
def create_course(course:schema.Create_course,db:Session=Depends(get_db)):
    new_cor=models.courses(**course.model_dump()) 
    new_cor.website=str(course.website)
    db.add(new_cor)
    db.commit()
    db.refresh(new_cor)
    return new_cor


@router.get("/", response_model=List[schema.course_response])
def course(db:Session=Depends(get_db)):
    course = db.query(models.courses).all()

    return course

@router.get("/{id}",response_model=schema.course_response)
def new_course(id:int,db:Session=Depends(get_db)):
    course=db.query(models.courses).filter(models.courses.id==id).first()
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"course with id {id} not found"
        )
    return course



@router.delete("/{id}",status_code=status.HTTP_200_OK,response_model=schema.course_response)
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



@router.put("/{id}",response_model=schema.course_response)
def updatedNewCourse(id:int,course:schema.Create_course,db:Session=Depends(get_db)):
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


# @router.get("/", response_model=List[schema.course_response])
# def course(db:Session=Depends(get_db)):
#     course = db.query(models.courses).all()

#     return course

# @router.get("/{id}",response_model=schema.course_response)
# def new_course(id:int,db:Session=Depends(get_db)):
#     course=db.query(models.courses).filter(models.courses.id==id).first()
#     if not course:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"course with id {id} not found"
#         )
#     return course


# @router.delete("/{id}",status_code=status.HTTP_200_OK,response_model=schema.course_response)
# def deleted(id:int,db:Session=Depends(get_db)):
#     course_query=db.query(models.courses).filter(models.courses.id==id)
#     delete_course=course_query.first()
#     if not delete_course:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"course with id {id} not found"
#         )
#     course_query.delete(synchronize_session=False)
#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)



# @router.put("/{id}",response_model=schema.course_response)
# def updatedNewCourse(id:int,course:schema.Create_course,db:Session=Depends(get_db)):
#     course_query=db.query(models.courses).filter(models.courses.id==id)
#     updated_course=course_query.first()
#     if not updated_course:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"course with id {id} not found"
#         )
#     updated_data=course.model_dump()
#     updated_data["website"]=str(updated_data["website"])
#     course_query.update(updated_data,synchronize_session=False)
#     db.commit()
#     db.refresh(updated_course)
#     return{"updated_course":updated_course}