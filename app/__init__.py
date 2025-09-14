    # app/init_db.py
from app.database.database import Base, engine
# importá los módulos con modelos para que SQLAlchemy los registre
import app.models.subjects
import app.models.users
import app.models.users_subjects

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas")

if __name__ == "__main__":
    create_tables()
