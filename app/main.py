import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import HTTPException
import os

# Definir el modelo de datos
Base = declarative_base()

class Candidato(Base):
    __tablename__ = "candidatos"

    id = Column(Integer, primary_key=True, index=True)
    dni = Column(String, unique=True, index=True)
    nombre = Column(String, index=True)
    apellido = Column(String, index=True)

# Configurar la base de datos SQLite
# Obtener la ruta absoluta de la carpeta 'database' dentro del directorio actual
DATABASE_DIR = os.path.join(os.getcwd(), 'database')

# Crear la carpeta 'database' si no existe
os.makedirs(DATABASE_DIR, exist_ok=True)

# Definir la URL de la base de datos con la ubicación en la carpeta 'database'
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DATABASE_DIR}/candidatos.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base.metadata.create_all(bind=engine)

# Crear la sesión de la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Inicializar la aplicación FastAPI
app = FastAPI()

# Definir el modelo de entrada para el endpoint /candidato
class CandidatoCreate(BaseModel):
    dni: str
    nombre: str
    apellido: str

# Definir el endpoint /candidato para agregar nuevos a la base de datos
@app.post("/candidato")
async def create_candidato(candidato: CandidatoCreate):
    db = SessionLocal()
    
    # Verificar si el DNI está duplicado
    if db.query(Candidato).filter(Candidato.dni == candidato.dni).first():
        raise HTTPException(status_code=400, detail="DNI duplicado")
    
    db_candidato = Candidato(**candidato.dict())
    db.add(db_candidato)
    db.commit()
    db.refresh(db_candidato)
    return db_candidato

# Endpoint para obtener todos los candidatos 
@app.get("/candidato")
async def get_candidatos():
    db = SessionLocal()
    candidatos = db.query(Candidato).all()
    return candidatos

# Protección del punto de entrada
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
