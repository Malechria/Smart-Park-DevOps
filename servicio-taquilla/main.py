import os
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from pydantic import BaseModel

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://admin:superpassword123@db:5432/smartpark")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class BoletoDB(Base):
    __tablename__ = "boletos"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, index=True)
    tipo = Column(String)
    precio = Column(Float)

Base.metadata.create_all(bind=engine)

class BoletoCreate(BaseModel):
    usuario_id: int
    tipo: str # Ej. "VIP", "General"
    precio: float

class BoletoResponse(BaseModel):
    id: int
    usuario_id: int
    tipo: str
    precio: float
    class Config:
        orm_mode = True

app = FastAPI(title="SmartPark - Servicio de Taquilla")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/comprar/", response_model=BoletoResponse)
def comprar_boleto(boleto: BoletoCreate, db: Session = Depends(get_db)):
    nuevo_boleto = BoletoDB(usuario_id=boleto.usuario_id, tipo=boleto.tipo, precio=boleto.precio)
    db.add(nuevo_boleto)
    db.commit()
    db.refresh(nuevo_boleto)
    return nuevo_boleto