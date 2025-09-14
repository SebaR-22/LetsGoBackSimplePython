from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.database.database import Base

class UserSubjects(Base):
    __tablename__ = "User_Subject"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("Users.id"), nullable=False) 
    subject_id = Column(Integer, ForeignKey("Subjects.id"), nullable=False)  
    
    # Evitar duplicados
    __table_args__ = (UniqueConstraint("user_id", "subject_id", name="_user_subject_uc"),)
    
    # Relaciones
    user = relationship("User", back_populates="user_subjects")
    subject = relationship("Subject", back_populates="user_subjects")