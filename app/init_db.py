from app.database.database import Base, engine
from app.models.users import User
from app.models.subjects import Subjects
from app.models.users_subjects import UserSubjects

# Crea todas las tablas si no existen
Base.metadata.create_all(bind=engine)

print("Tablas creadas correctamente")
