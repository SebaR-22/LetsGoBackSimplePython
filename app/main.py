from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db, engine, Base
from app.api.routes import user, subject, user_subject
from sqlalchemy import text

# Importar todos los modelos para que SQLAlchemy los conozca
from app.models.subjects import Subject
from app.models.users import User
from app.models.users_subjects import UserSubjects

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Crear la aplicación FastAPI
app = FastAPI(
    title="Sistema Educativo API",
    description="API para gestionar usuarios y materias",
    version="1.0.0",
)

# Ruta para probar la conexión a la base de datos
@app.get("/health")
async def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {
            "status": "healthy",
            "database": "connected",
            "message": "La aplicación está funcionando correctamente",
        }
    except Exception as e:
        return {"status": "unhealthy", "database": "disconnected", "error": str(e)}

# Incluir routers
app.include_router(user.router)
app.include_router(subject.router)
app.include_router(user_subject.router)

@app.get("/")
async def root():
    return {"message": "Sistema Educativo API - Funcionando correctamente"}