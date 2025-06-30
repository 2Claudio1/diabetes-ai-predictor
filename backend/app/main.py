from fastapi import FastAPI, Depends, APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import func
from .database import SessionLocal, init_db
from . import models, schemas
from datetime import datetime
from typing import Optional

app = FastAPI()

# Prefijo y etiquetas para las rutas
router = APIRouter(prefix="/api", tags=["PrediccionesDiabetes"])

# Configuración de CORS: tu frontend local, puedes agregar más dominios si quieres
origins = [
    "http://localhost:5173",
    # "*" # para todos, menos seguro
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

# Evento que se ejecuta al iniciar el servidor
@app.on_event("startup")
def startup_event():
    # Inicializa la base de datos (crea tablas)
    init_db()
    db = SessionLocal()
    try:
        # Si la tabla está vacía, insertar datos demo
        if db.query(models.PrediccionDiabetes).count() == 0:
            datos_demo = [
                # Tus datos demo aquí, tal cual los tienes
                # (omito para no repetir)
            ]
            for item in datos_demo:
                registro = models.PrediccionDiabetes(**item)
                db.add(registro)
            db.commit()
    finally:
        db.close()

# POST: Guardar nuevo registro
@router.post("/guardar-datos/", response_model=schemas.PrediccionDiabetes)
def guardar_datos(datos: schemas.PrediccionDiabetesCreate, db: Session = Depends(get_db)):
    nuevo = models.PrediccionDiabetes(**datos.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

# GET: Obtener todos los registros
@router.get("/todos-datos/", response_model=list[schemas.PrediccionDiabetes])
def obtener_todos(db: Session = Depends(get_db)):
    return db.query(models.PrediccionDiabetes).all()

# GET: Obtener registro por ID
@router.get("/obtener-por-id/{id}", response_model=schemas.PrediccionDiabetes)
def obtener_por_id(id: int, db: Session = Depends(get_db)):
    registro = db.query(models.PrediccionDiabetes).filter(models.PrediccionDiabetes.id == id).first()
    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado.")
    return registro

# GET: Filtrar registros por país
@router.get("/filtrar-por-pais/{pais}", response_model=list[schemas.PrediccionDiabetes])
def filtrar_por_pais(pais: str, db: Session = Depends(get_db)):
    return db.query(models.PrediccionDiabetes).filter(models.PrediccionDiabetes.pais == pais).all()

# DELETE: Eliminar registro por ID
@router.delete("/eliminar-por-id/{id}")
def eliminar_por_id(id: int, db: Session = Depends(get_db)):
    registro = db.query(models.PrediccionDiabetes).filter(models.PrediccionDiabetes.id == id).first()
    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado.")
    db.delete(registro)
    db.commit()
    return {"mensaje": f"Registro con id {id} eliminado correctamente"}

# GET: Promedio de diabetes_bin por país
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

# GET: Promedio de diabetes_bin agrupado por año, mes y continente. Filtro opcional por continente.
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
    # Resto igual
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
