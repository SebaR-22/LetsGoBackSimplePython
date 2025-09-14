from pydantic import BaseModel

class UserSubjectCreate(BaseModel):
    user_id: int
    subject_id: int

class UserSubject(BaseModel):
    id: int
    user_id: int
    subject_id: int
    
    class Config:
        from_attributes = True

# Schema con relaciones incluidas
class UserSubjectDetail(BaseModel):
    id: int
    user_id: int
    subject_id: int
    user: dict 
    subject: dict  
    
    class Config:
        from_attributes = True