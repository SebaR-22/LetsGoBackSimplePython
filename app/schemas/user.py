from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: str

# Para crear un usuario nuevo
class UserCreate(UserBase):
    password: str

# Para actualizar usuario
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role: Optional[str] = None

# Lo que devolvemos al cliente
class User(UserBase):
    id: int
    
    class Config:
        from_attributes = True

# Para login
class LoginSchema(BaseModel):
    email: EmailStr
    password: str