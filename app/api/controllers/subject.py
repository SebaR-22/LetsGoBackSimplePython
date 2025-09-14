from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.subjects import Subject
from app.schemas.subject import SubjectCreate, SubjectUpdate

def get_subjects(db: Session):
    return db.query(Subject).all()

def get_subject_by_id(db: Session, subject_id: int):
    subject = db.query(Subject).filter(Subject.id == subject_id).first()
    if not subject:
        raise HTTPException(status_code=404, detail="Materia no encontrada")
    return subject

def create_subject(db: Session, subject: SubjectCreate):
    # Verificar si ya existe una materia con el mismo nombre
    existing_subject = db.query(Subject).filter(Subject.name == subject.name).first()
    if existing_subject:
        raise HTTPException(status_code=400, detail="Ya existe una materia con ese nombre")
    
    db_subject = Subject(
        name=subject.name,
        description=subject.description
    )
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject

def update_subject(db: Session, subject_id: int, subject_update: SubjectUpdate):
    db_subject = get_subject_by_id(db, subject_id)
    
    update_data = subject_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_subject, field, value)
    
    db.commit()
    db.refresh(db_subject)
    return db_subject

def delete_subject(db: Session, subject_id: int):
    db_subject = get_subject_by_id(db, subject_id)
    db.delete(db_subject)
    db.commit()
    return db_subject