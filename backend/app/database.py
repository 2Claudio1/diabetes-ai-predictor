from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
import time
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:unir1234@db:5432/diabetes_predictor"

def get_engine():
    max_attempts = 5
    for attempt in range(max_attempts):
        try:
            engine = create_engine(SQLALCHEMY_DATABASE_URL)
            # Probamos la conexión con text() para hacerlo ejecutable
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            logger.info("Conexión a la base de datos establecida correctamente")
            return engine
        except OperationalError as e:
            logger.error(f"Intento {attempt + 1} fallido: {str(e)}")
            if attempt == max_attempts - 1:
                raise
            time.sleep(5)

engine = get_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def init_db():
    from . import models
    Base.metadata.create_all(bind=engine)