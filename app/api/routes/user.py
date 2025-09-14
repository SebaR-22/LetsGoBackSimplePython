from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.user import User, UserCreate, UserUpdate, LoginSchema
from app.api.controllers import user as user_controller
from app.database.database import get_db
from app.security.jwt_manager import create_access_token

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=List[User])
def get_users(db: Session = Depends(get_db)):
    return user_controller.get_users(db)

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return user_controller.get_user_by_id(db, user_id)

@router.post("/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_controller.create_user(db, user)

@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    return user_controller.update_user(db, user_id, user_update)

@router.delete("/{user_id}", response_model=User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return user_controller.delete_user(db, user_id)

@router.post("/login/")
def login(user: LoginSchema, db: Session = Depends(get_db)):
    db_user = user_controller.authenticate_user(db, user.email, user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="Email o contraseña incorrectos")
    
    # Crear token JWT
    access_token = create_access_token(data={"user_id": db_user.id, "email": db_user.email})
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": db_user.id,
            "name": db_user.name,
            "email": db_user.email,
            "role": db_user.role
        }
    }