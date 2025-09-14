"""
Script para crear todas las tablas en la base de datos
Ejecuta este archivo una vez para crear las tablas iniciales
"""

from app.database.database import engine, Base
from app.models.users import User
from app.models.users_subjects import UserSubjects
from app.models.subjects import Subjects


def create_tables():
    """Crear todas las tablas definidas en los modelos"""
    try:
        print("Creando tablas...")
        Base.metadata.create_all(bind=engine)
        print("creadas exitosamente!")
        
        # Verificar que las tablas existen
        from sqlalchemy import inspect
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        print(f"Tablas en la base de datos: {tables}")

        for t in ["Users", "Subjects", "User_Subject"]:
            if t in tables:
                print(f"✅ Tabla '{t}' creada correctamente")
            else:
                print(f"❌ Error: Tabla '{t}' no fue creada")
            
    except Exception as e:
        print(f"❌ Error al crear las tablas: {str(e)}")

if __name__ == "__main__":
    create_tables()