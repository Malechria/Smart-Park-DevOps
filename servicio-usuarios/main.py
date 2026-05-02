import os
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from pydantic import BaseModel

# 1. Configuración de la Base de Datos
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://admin:superpassword123@db:5432/smartpark")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 2. Modelo de la Base de Datos (Tabla)
class UsuarioDB(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    email = Column(String, unique=True, index=True)

# Crea las tablas en la base de datos si no existen
Base.metadata.create_all(bind=engine)

# 3. Modelos de validación (Pydantic)
class UsuarioCreate(BaseModel):
    nombre: str
    email: str

class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    email: str
    class Config:
        orm_mode = True

# 4. Inicialización de la App
app = FastAPI(title="SmartPark - Servicio de Usuarios")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 5. Endpoints
@app.post("/usuarios/", response_model=UsuarioResponse)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    db_user = db.query(UsuarioDB).filter(UsuarioDB.email == usuario.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="El correo ya está registrado")
    
    nuevo_usuario = UsuarioDB(nombre=usuario.nombre, email=usuario.email)
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

@app.get("/usuarios/{user_id}", response_model=UsuarioResponse)
def obtener_usuario(user_id: int, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioDB).filter(UsuarioDB.id == user_id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario