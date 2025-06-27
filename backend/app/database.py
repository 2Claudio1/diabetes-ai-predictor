from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Cambia por tu usuario y contraseña de docker compose
DATABASE_URL = "postgresql://postgres:unir1234@db:5432/diabetes_predictor"

Base = declarative_base()
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear todas las tablas
def init_db():
    from . import models
    Base.metadata.create_all(bind=engine)