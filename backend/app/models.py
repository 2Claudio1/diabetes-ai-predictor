from sqlalchemy import Column, Integer, String, Float, DateTime, func
from .database import Base

class PrediccionDiabetes(Base):
    __tablename__ = "predicciones_diabetes"

    id = Column(Integer, primary_key=True, index=True)
    diabetes_bin = Column(Integer, nullable=False)  # Predicción generada en backend
    sexo = Column(Integer, nullable=False)
    grupo_edad = Column(Integer, nullable=False)
    grupo_racial = Column(Integer, nullable=False)
    nivel_educativo = Column(Integer, nullable=False)
    ingresos_grupo = Column(Integer, nullable=False)
    altura = Column(Float, nullable=False)
    peso = Column(Float, nullable=False)
    presion_alta = Column(Integer, nullable=False)
    colesterol_alto = Column(Integer, nullable=False)
    control_colesterol = Column(Integer, nullable=False)
    bmi = Column(Float, nullable=False)
    fumo_100_cigs = Column(Integer, nullable=False)
    historial_acv = Column(Integer, nullable=False)
    historial_cardiaco = Column(Integer, nullable=False)
    dificultad_caminar = Column(Integer, nullable=False)
    actividad_fisica = Column(Integer, nullable=False)
    actividad_300min = Column(Integer, nullable=False)
    actividad_muscular = Column(Integer, nullable=False)
    frecuencia_frutas = Column(Integer, nullable=False)
    frecuencia_verduras = Column(Integer, nullable=False)
    salud_general = Column(Integer, nullable=False)
    dias_mala_salud_fisica = Column(Integer, nullable=False)
    dias_mala_salud_mental = Column(Integer, nullable=False)
    continente = Column(String(30), nullable=False)
    pais = Column(String(100), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
