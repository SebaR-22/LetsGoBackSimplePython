from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException
from app.models.users_subjects import UserSubjects
from app.schemas.user_subject import UserSubjectCreate

def get_user_subjects(db: Session):
    return db.query(UserSubjects).options(
        joinedload(UserSubjects.user),
        joinedload(UserSubjects.subject)
    ).all()

def get_user_subjects_by_user_id(db: Session, user_id: int):
    return db.query(UserSubjects).filter(
        UserSubjects.user_id == user_id
    ).options(joinedload(UserSubjects.subject)).all()

def get_subject_users_by_subject_id(db: Session, subject_id: int):
    return db.query(UserSubjects).filter(
        UserSubjects.subject_id == subject_id
    ).options(joinedload(UserSubjects.user)).all()

def create_user_subject(db: Session, user_subject: UserSubjectCreate):
    # Validación para no duplicar relaciones
    existing = db.query(UserSubjects).filter(
        UserSubjects.user_id == user_subject.user_id,
        UserSubjects.subject_id == user_subject.subject_id
    ).first()
    
    if existing:
        raise HTTPException(status_code=400, detail="La relación ya existe")
    
    db_us = UserSubjects(
        user_id=user_subject.user_id,
        subject_id=user_subject.subject_id
    )
    db.add(db_us)
    db.commit()
    db.refresh(db_us)
    return db_us

def delete_user_subject(db: Session, user_id: int, subject_id: int):
    db_us = db.query(UserSubjects).filter(
        UserSubjects.user_id == user_id,
        UserSubjects.subject_id == subject_id
    ).first()
    
    if not db_us:
        raise HTTPException(status_code=404, detail="Relación no encontrada")
    
    db.delete(db_us)
    db.commit()
    return db_us