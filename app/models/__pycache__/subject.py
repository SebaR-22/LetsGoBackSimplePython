## id nombre Id PROFE 

# app/models/subject.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class Subject(Base):
    _tablename_ = "profesores"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    users = relationship("SubjectUser", back_populates="subject")