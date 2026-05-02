import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # <-- Importante
from pydantic import BaseModel

app = FastAPI(title="SmartPark - Servicio de Taquilla")

# --- CONFIGURACIÓN DE CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo para recibir la compra
class TicketCreate(BaseModel):
    usuario_id: int
    tipo: str

# Contador simple para simular IDs de boletos
ticket_id_counter = 100

@app.get("/")
def read_root():
    return {"status": "ok", "servicio": "SmartPark - Taquilla"}

@app.post("/tickets/")
def emitir_ticket(ticket: TicketCreate):
    global ticket_id_counter
    ticket_id_counter += 1
    
    # Aquí en un sistema real, primero verificaríamos en el puerto 8001 si el usuario existe
    return {
        "id": ticket_id_counter,
        "usuario_id": ticket.usuario_id,
        "tipo": ticket.tipo,
        "mensaje": "¡Boleto emitido con éxito!"
    }