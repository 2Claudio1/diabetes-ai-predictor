from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PrediccionDiabetesCreate(BaseModel):
    diabetes_bin: Optional[int] = None
    sexo: Optional[int] = None
    grupo_edad: Optional[int] = None
    grupo_racial: Optional[int] = None
    nivel_educativo: Optional[int] = None
    categoria_ingresos: Optional[int] = None
    altura: Optional[float] = None
    peso: Optional[float] = None
    presion_alta: Optional[int] = None
    colesterol_alto: Optional[int] = None
    control_colesterol: Optional[int] = None
    bmi: Optional[float] = None
    fumo_100_cigs: Optional[int] = None
    historial_acv: Optional[int] = None
    historial_cardiaco: Optional[int] = None
    dificultad_caminar: Optional[int] = None
    actividad_fisica: Optional[int] = None
    actividad_300min: Optional[int] = None
    actividad_muscular: Optional[int] = None
    frecuencia_frutas: Optional[int] = None
    frecuencia_verduras: Optional[int] = None
    salud_general: Optional[int] = None
    dias_mala_salud_fisica: Optional[int] = None
    dias_mala_salud_mental: Optional[int] = None
    continente: Optional[str] = None
    pais: Optional[str] = None
    region: Optional[str] = None
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True
