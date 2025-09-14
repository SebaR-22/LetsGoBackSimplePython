from pydantic import BaseModel
from typing import Optional

class SubjectBase(BaseModel):
    name: str
    description: Optional[str] = None

class SubjectCreate(SubjectBase):
    pass

class SubjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class Subject(SubjectBase):
    id: int
    
    class Config:
        from_attributes = True