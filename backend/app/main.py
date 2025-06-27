from fastapi import FastAPI, Depends, APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import func
from .database import SessionLocal, init_db
from . import models, schemas
from datetime import datetime
from .data_dummy import datos_demo

app = FastAPI()
router = APIRouter(prefix="/api", tags=["PrediccionesDiabetes"])

origins = [
    "http://localhost:5173",  # tu frontend
    # o "*" para todos, pero es menos seguro
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def startup_event():
    init_db()
    db = SessionLocal()
    if db.query(models.PrediccionDiabetes).count() == 0:
        for item in datos_demo:
            registro = models.PrediccionDiabetes(**item)
            db.add(registro)
        db.commit()
    db.close()

@router.post("/guardar-datos/")
def guardar_datos(datos: schemas.PrediccionDiabetesCreate, db: Session = Depends(get_db)):
    nuevo = models.PrediccionDiabetes(**datos.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return {"id": nuevo.id, "mensaje": "Datos guardados exitosamente"}

@router.get("/todos-datos/")
def obtener_todos(db: Session = Depends(get_db)):
    return db.query(models.PrediccionDiabetes).all()

@router.get("/obtener-por-id/{id}")
def obtener_por_id(id: int, db: Session = Depends(get_db)):
    registro = db.query(models.PrediccionDiabetes).filter(models.PrediccionDiabetes.id == id).first()
    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado.")
    return registro

@router.get("/filtrar-por-pais/{pais}")
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
    # Agrupar por país y sacar promedio de diabetes_bin
    resultados = (
        db.query(
            models.PrediccionDiabetes.pais,
            func.avg(models.PrediccionDiabetes.diabetes_bin).label("promedio_diabetes_bin"),
            func.count(models.PrediccionDiabetes.id).label("total_registros")
        )
        .group_by(models.PrediccionDiabetes.pais)
        .all()
    )

    # Formatear salida
    return [
        {
            "pais": r.pais,
            "promedio_diabetes_bin": float(r.promedio_diabetes_bin),
            "total_registros": r.total_registros
        }
        for r in resultados
    ]
    
#Al final, para crear las rutas
app.include_router(router)