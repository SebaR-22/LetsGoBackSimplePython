from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.user_subject import UserSubject, UserSubjectCreate
from app.api.controllers import user_subject as user_subject_controller
from app.database.database import get_db

router = APIRouter(prefix="/user-subjects", tags=["User-Subjects"])

@router.get("/", response_model=List[UserSubject])
def get_user_subjects(db: Session = Depends(get_db)):
    return user_subject_controller.get_user_subjects(db)

@router.get("/user/{user_id}", response_model=List[UserSubject])
def get_subjects_by_user(user_id: int, db: Session = Depends(get_db)):
    return user_subject_controller.get_user_subjects_by_user_id(db, user_id)

@router.get("/subject/{subject_id}", response_model=List[UserSubject])
def get_users_by_subject(subject_id: int, db: Session = Depends(get_db)):
    return user_subject_controller.get_subject_users_by_subject_id(db, subject_id)

@router.post("/", response_model=UserSubject)
def create_user_subject(user_subject: UserSubjectCreate, db: Session = Depends(get_db)):
    return user_subject_controller.create_user_subject(db, user_subject)

@router.delete("/{user_id}/{subject_id}", response_model=UserSubject)
def delete_user_subject(user_id: int, subject_id: int, db: Session = Depends(get_db)):
    return user_subject_controller.delete_user_subject(db, user_id, subject_id)