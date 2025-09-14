# app/database/__init__.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Lee la URL de la base de datos desde una variable de entorno o usa la predeterminada
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:admin@localhost:5432/proyecto_db")

# Crea el motor (engine)
engine = create_engine(DATABASE_URL)

# Crea la base declarativa
Base = declarative_base()

# Crea la sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Función para obtener la sesión de base de datos (usada en los endpoints)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()