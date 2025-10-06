from fastapi import FastAPI, Depends, APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import func
from .database import SessionLocal, init_db
from . import models, schemas
from datetime import datetime
from typing import Optional
import time
import logging
from .data_dummy import datos_demo

import joblib
import numpy as np
from pathlib import Path

# Para testes
import random

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Prefijo y etiquetas para las rutas
router = APIRouter(prefix="/api", tags=["PrediccionesDiabetes"])

# Configuración de CORS
origins = [
    "http://localhost:5173",
    "http://localhost:8000",
    # Puedes agregar más dominios permitidos aquí
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "xgb_model.pkl"
SCALER_PATH = BASE_DIR / "models" / "minmaxscaler.pkl"

# Cargar MinMaxScaler
scaler = joblib.load(SCALER_PATH)

# Cargar modelo XGBoost entrenado
modelo_xgb = joblib.load(MODEL_PATH)

# Evento que se ejecuta al iniciar el servidor con reintentos para conectar a la DB
@app.on_event("startup")
async def startup_event():
    max_attempts = 5
    for attempt in range(max_attempts):
        try:
            logger.info(f"Intentando conectar a la base de datos (intento {attempt + 1}/{max_attempts})")
            init_db()
            db = SessionLocal()
            
            # Insertar datos demo si la tabla está vacía
            if db.query(models.PrediccionDiabetes).count() == 0:
                for item in datos_demo:
                    registro = models.PrediccionDiabetes(**item)
                    db.add(registro)
                db.commit()
                logger.info("Datos demo insertados correctamente")
            break
        except Exception as e:
            logger.error(f"Error en intento {attempt + 1}: {str(e)}")
            if attempt == max_attempts - 1:
                logger.error("No se pudo conectar a la base de datos después de varios intentos")
                raise
            time.sleep(5)
        finally:
            db.close()

# Rutas de la API

#@router.post("/guardar-datos/", response_model=schemas.PrediccionDiabetes)
@router.post("/guardar-datos/", response_model=int)
def guardar_datos(datos: schemas.PrediccionDiabetesCreate, db: Session = Depends(get_db)):
    # Convertir los datos a diccionario
    datos_dict = datos.dict()

    # --- Crear el array de entrada en el mismo orden que el modelo fue entrenado ---
    features = np.array([[
        datos_dict["presion_alta"],
        datos_dict["colesterol_alto"],
        datos_dict["bmi"],
        datos_dict["fumo_100_cigs"],
        datos_dict["historial_acv"],
        datos_dict["historial_cardiaco"],
        datos_dict["actividad_fisica"],
        datos_dict["salud_general"],
        datos_dict["dias_mala_salud_fisica"],
        datos_dict["dias_mala_salud_mental"],
        datos_dict["dificultad_caminar"],
        datos_dict["sexo"],
        datos_dict["grupo_edad"],
        datos_dict["nivel_educativo"],
        datos_dict["grupo_racial"],
        datos_dict["actividad_300_min"],
        datos_dict["actividad_muscular"],
        datos_dict["frecuencia_frutas"],
        datos_dict["frecuencia_verduras"],
        datos_dict["ingresos_grupo"]
    ]])

    # Escalar los datos con MinMaxScaler
    features_scaled = scaler.transform(features)
    
    # Hacer la predicción
    try:
        prediccion = int(modelo_xgb.predict(features_scaled)[0])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al hacer la predicción: {str(e)}")

    # Guardar predicción en el diccionario y en la DB
    datos_dict['diabetes_bin'] = prediccion
    nuevo = models.PrediccionDiabetes(**datos_dict)

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    return prediccion


@router.get("/todos-datos/", response_model=list[schemas.PrediccionDiabetes])
def obtener_todos(db: Session = Depends(get_db)):
    return db.query(models.PrediccionDiabetes).all()

@router.get("/obtener-por-id/{id}", response_model=schemas.PrediccionDiabetes)
def obtener_por_id(id: int, db: Session = Depends(get_db)):
    registro = db.query(models.PrediccionDiabetes).filter(models.PrediccionDiabetes.id == id).first()
    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado.")
    return registro

@router.get("/filtrar-por-pais/{pais}", response_model=list[schemas.PrediccionDiabetes])
def filtrar_por_pais(pais: str, db: Session = Depends(get_db)):
    return db.query(models.PrediccionDiabetes).filter(models.PrediccionDiabetes.pais == pais).all()

@router.delete("/eliminar-por-id/{id}")
def eliminar_por_id(id: int, db: Session = Depends(get_db)):
    registro = db.query(models.PrediccionDiabetes).filter(models.PrediccionDiabetes.id == id).first()
    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado.")
    db.delete(registro)
    db.commit()
    return {"mensaje": f"Registro con id {id} eliminado correctamente"}

@router.get("/promedio-diabetes-por-pais/")
def promedio_diabetes_por_pais(db: Session = Depends(get_db)):
    resultados = (
        db.query(
            models.PrediccionDiabetes.pais,
            func.avg(models.PrediccionDiabetes.diabetes_bin).label("promedio_diabetes_bin"),
            func.count(models.PrediccionDiabetes.id).label("total_registros")
        )
        .group_by(models.PrediccionDiabetes.pais)
        .all()
    )
    return [
        {
            "pais": r.pais,
            "promedio_diabetes_bin": float(r.promedio_diabetes_bin),
            "total_registros": r.total_registros
        }
        for r in resultados
    ]

@router.get("/promedio-diabetes-tiempo/")
def promedio_diabetes_tiempo(
    continente: Optional[str] = None,
    anio: Optional[int] = None,
    db: Session = Depends(get_db)
):
    query = db.query(
        func.extract('year', models.PrediccionDiabetes.created_at).label('anio'),
        func.extract('month', models.PrediccionDiabetes.created_at).label('mes'),
        models.PrediccionDiabetes.continente,
        func.avg(models.PrediccionDiabetes.diabetes_bin).label('promedio_diabetes_bin'),
        func.count(models.PrediccionDiabetes.id).label('total_registros')
    )
    if continente:
        query = query.filter(models.PrediccionDiabetes.continente == continente)
    if anio:
        query = query.filter(func.extract('year', models.PrediccionDiabetes.created_at) == anio)
    query = query.group_by('anio', 'mes', models.PrediccionDiabetes.continente).order_by('anio', 'mes')
    resultados = query.all()
    return [
        {
            "anio": int(r.anio),
            "mes": int(r.mes),
            "continente": r.continente,
            "promedio_diabetes_bin": float(r.promedio_diabetes_bin),
            "total_registros": int(r.total_registros)
        }
        for r in resultados
    ]

# Incluir el router en la app principal
app.include_router(router)
