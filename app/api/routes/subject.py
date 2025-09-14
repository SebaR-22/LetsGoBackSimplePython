from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.subject import Subject, SubjectCreate, SubjectUpdate
from app.api.controllers import subject as subject_controller
from app.database.database import get_db

router = APIRouter(prefix="/subjects", tags=["Subjects"])

@router.get("/", response_model=List[Subject])
def get_subjects(db: Session = Depends(get_db)):
    return subject_controller.get_subjects(db)

@router.get("/{subject_id}", response_model=Subject)
def get_subject(subject_id: int, db: Session = Depends(get_db)):
    return subject_controller.get_subject_by_id(db, subject_id)

@router.post("/", response_model=Subject)
def create_subject(subject: SubjectCreate, db: Session = Depends(get_db)):
    return subject_controller.create_subject(db, subject)

@router.put("/{subject_id}", response_model=Subject)
def update_subject(subject_id: int, subject_update: SubjectUpdate, db: Session = Depends(get_db)):
    return subject_controller.update_subject(db, subject_id, subject_update)

@router.delete("/{subject_id}", response_model=Subject)
def delete_subject(subject_id: int, db: Session = Depends(get_db)):
    return subject_controller.delete_subject(db, subject_id)