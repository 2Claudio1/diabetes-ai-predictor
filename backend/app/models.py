from sqlalchemy import Column, Integer, String, Float, DateTime, func
from .database import Base

class PrediccionDiabetes(Base):
    __tablename__ = "predicciones_diabetes"

    id = Column(Integer, primary_key=True, index=True)
    diabetes_bin = Column(Integer, nullable=True)  # Resultado binario de la predicción
    sexo = Column(Integer, nullable=True)
    grupo_edad = Column(Integer, nullable=True)
    grupo_racial = Column(Integer, nullable=True)
    nivel_educativo = Column(Integer, nullable=True)
    categoria_ingresos = Column(Integer, nullable=True)
    altura = Column(Float, nullable=True)
    peso = Column(Float, nullable=True)
    presion_alta = Column(Integer, nullable=True)
    colesterol_alto = Column(Integer, nullable=True)
    control_colesterol = Column(Integer, nullable=True)
    bmi = Column(Float, nullable=True)
    fumo_100_cigs = Column(Integer, nullable=True)
    historial_acv = Column(Integer, nullable=True)
    historial_cardiaco = Column(Integer, nullable=True)
    dificultad_caminar = Column(Integer, nullable=True)
    actividad_fisica = Column(Integer, nullable=True)
    actividad_300min = Column(Integer, nullable=True)
    actividad_muscular = Column(Integer, nullable=True)
    frecuencia_frutas = Column(Integer, nullable=True)
    frecuencia_verduras = Column(Integer, nullable=True)
    salud_general = Column(Integer, nullable=True)
    dias_mala_salud_fisica = Column(Integer, nullable=True)
    dias_mala_salud_mental = Column(Integer, nullable=True)
    continente = Column(String(30), nullable=True)
    pais = Column(String(100), nullable=True)
    region = Column(String(100), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
