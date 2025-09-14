from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database import Base


class SubjectUser(Base):
    _tablename_ = "Materia-usuario"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    role = Column(String, nullable=False)  # "student" o "teacher" en esta materia

    user = relationship("User", back_populates="subjects")
    subject = relationship("Subject", back_populates="users")