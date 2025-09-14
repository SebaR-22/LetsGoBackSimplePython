from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.database import Base

class Subject(Base):  # Cambié a singular
    __tablename__ = "Subjects"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)  
    description = Column(String(255), nullable=True) 
    
    # Relación hacia la tabla asociativa
    user_subjects = relationship("UserSubjects", back_populates="subject", cascade="all, delete-orphan")