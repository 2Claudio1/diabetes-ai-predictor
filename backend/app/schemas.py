from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class PrediccionDiabetesBase(BaseModel):
    sexo: int = Field(..., description="Sexo del usuario (1=masculino, 2=femenino)")
    grupo_edad: int = Field(..., description="Grupo de edad")
    grupo_racial: int = Field(..., description="Grupo racial")
    nivel_educativo: int = Field(..., description="Nivel educativo")
    ingresos_grupo: int = Field(..., description="Grupo de ingresos")
    altura: float = Field(..., description="Altura en metros")
    peso: float = Field(..., description="Peso en kilogramos")
    presion_alta: int = Field(..., description="Hipertensión (1=Sí, 0=No)")
    colesterol_alto: int = Field(..., description="Colesterol alto (1=Sí, 0=No)")
    control_colesterol: int = Field(..., description="Control de colesterol (1=Sí, 0=No)")
    bmi: float = Field(..., description="Índice de masa corporal")
    fumo_100_cigs: int = Field(..., description="Ha fumado 100 cigarrillos o más (1=Sí, 0=No)")
    historial_acv: int = Field(..., description="Historial de accidente cerebrovascular")
    historial_cardiaco: int = Field(..., description="Historial cardíaco")
    dificultad_caminar: int = Field(..., description="Dificultad para caminar")
    actividad_fisica: int = Field(..., description="Actividad física")
    actividad_300min: int = Field(..., description="Cumplimiento de 300 minutos de actividad física semanal")
    actividad_muscular: int = Field(..., description="Ejercicio muscular")
    frecuencia_frutas: int = Field(..., description="Frecuencia de consumo de frutas")
    frecuencia_verduras: int = Field(..., description="Frecuencia de consumo de verduras")
    salud_general: int = Field(..., description="Percepción general de salud")
    dias_mala_salud_fisica: int = Field(..., description="Días de mala salud física en el último mes")
    dias_mala_salud_mental: int = Field(..., description="Días de mala salud mental en el último mes")
    continente: str = Field(..., description="Continente")
    pais: str = Field(..., description="País")
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class PrediccionDiabetesCreate(PrediccionDiabetesBase):
    pass

class PrediccionDiabetes(PrediccionDiabetesBase):
    id: int
    diabetes_bin: int = Field(..., description="Predicción de diabetes (0 = no, 1 = sí)")

    class Config:
        orm_mode = True
