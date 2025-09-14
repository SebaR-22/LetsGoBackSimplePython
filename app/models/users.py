from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.database import Base

class User(Base):
    __tablename__ = "Users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)  
    email = Column(String(100), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False)  
    
    # Relación hacia la tabla asociativa
    user_subjects = relationship("UserSubjects", back_populates="user", cascade="all, delete-orphan")