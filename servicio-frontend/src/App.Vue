<template>
  <div class="main-container no-print">
    <header class="fade-in-down">
      <div class="logo-container">
        <span class="rollercoaster-emoji">🎢</span>
      </div>
      <h1>SmartPark Dashboard</h1>
      <p class="subtitle">Sistema de Entrega de Software</p>
    </header>

    <div class="grid">
      <!-- Módulo de Usuarios -->
      <section class="card slide-up-1">
        <div class="card-header users">
          <span class="icon">👤</span>
          <h2>Registro de Visitantes</h2>
        </div>
        <div class="card-body">
          <div class="input-group">
            <input v-model="userForm.nombre" placeholder="Nombre completo" />
            <div class="input-line"></div>
          </div>
          <div class="input-group">
            <input v-model="userForm.email" placeholder="correo@ejemplo.com" />
            <div class="input-line"></div>
          </div>
          <button @click="crearUsuario" class="btn-primary">Registrar Usuario</button>
          
          <transition name="bounce">
            <p v-if="userMsg" :class="statusClass">{{ userMsg }}</p>
          </transition>
        </div>
      </section>

      <!-- Módulo de Taquilla -->
      <section class="card slide-up-2">
        <div class="card-header tickets">
          <span class="icon">🎟️</span>
          <h2>Venta de Boletos</h2>
        </div>
        <div class="card-body">
          <div class="input-group">
            <input v-model="ticketForm.usuario_id" type="number" placeholder="ID del Usuario" />
            <div class="input-line"></div>
          </div>
          <div class="input-group">
            <select v-model="ticketForm.tipo">
              <option value="General">General ($500)</option>
              <option value="VIP">VIP ($1200)</option>
              <option value="Niños">Niños ($300)</option>
            </select>
            <div class="input-line"></div>
          </div>
          <button @click="comprarBoleto" class="btn-success">Emitir Boleto</button>
          
          <!-- Botón de Impresión -->
          <transition name="fade">
            <button v-if="ultimoTicket" @click="imprimirBoleto" class="btn-print">
              🖨️ Imprimir Ticket #{{ ultimoTicket.id }}
            </button>
          </transition>
          
          <transition name="bounce">
            <p v-if="ticketMsg" :class="statusClass">{{ ticketMsg }}</p>
          </transition>
        </div>
      </section>
    </div>
  </div>


  <div v-if="ultimoTicket" class="ticket-visual print-only">
    <div class="ticket-header">
      <div class="logo">🎢 SmartPark</div>
      <div class="ticket-id">ID: {{ ultimoTicket.id }}</div>
    </div>
    <div class="ticket-content">
      <p><strong>TIPO:</strong> {{ ultimoTicket.tipo }}</p>
      <p><strong>USUARIO:</strong> {{ ultimoTicket.usuario_id }}</p>
      <p><strong>FECHA:</strong> {{ new Date().toLocaleDateString() }}</p>
      <div class="barcode">|||| | || ||| | ||| | ||</div>
    </div>
    <div class="ticket-footer">
      ¡Disfruta tu aventura en el parque!
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const userForm = ref({ nombre: '', email: '' })
const ticketForm = ref({ usuario_id: '', tipo: 'General' })
const userMsg = ref('')
const ticketMsg = ref('')
const ultimoTicket = ref(null)
const statusClass = ref('')

const USERS_API = "http://localhost:8001"
const TICKETS_API = "http://localhost:8002"

const crearUsuario = async () => {
  try {
    const res = await axios.post(`${USERS_API}/usuarios/`, userForm.value)
    userMsg.value = `✅ Registrado: ID ${res.data.id}`
    statusClass.value = 'text-success alert-box'
  } catch (e) { 
    userMsg.value = '❌ Error de conexión o correo duplicado'; 
    statusClass.value = 'text-error alert-box' 
  }
}

const comprarBoleto = async () => {
  try {
    const res = await axios.post(`${TICKETS_API}/tickets/`, ticketForm.value)
    ultimoTicket.value = res.data
    ticketMsg.value = `🎫 Boleto generado exitosamente.`
    statusClass.value = 'text-success alert-box'
  } catch (e) { 
    ticketMsg.value = '❌ Error al emitir'; 
    statusClass.value = 'text-error alert-box' 
  }
}

const imprimirBoleto = () => {
  window.print() 
}
</script>

<style>

:root {
  --primary: #4f46e5;
  --primary-hover: #4338ca;
  --success: #10b981;
  --success-hover: #059669;
  --error: #ef4444;
  --bg-gradient: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
  --card-bg: rgba(255, 255, 255, 0.95);
}

body { 
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; 
  background: var(--bg-gradient); 
  min-height: 100vh;
  margin: 0; 
  color: #1e293b; 
}

.main-container { 
  max-width: 900px; 
  margin: 40px auto; 
  padding: 0 20px; 
}


header { 
  text-align: center; 
  margin-bottom: 50px; 
}
.logo-container {
  display: inline-block;
  background: rgb(255, 255, 255);
  padding: 15px;
  border-radius: 50%;
  box-shadow: 0 4px 6px rgba(0,0,0,0.05);
  margin-bottom: 10px;
  transition: transform 0.3s ease;
}
.logo-container:hover {
  transform: scale(1.1) rotate(5deg);
}
.rollercoaster-emoji { font-size: 2.5rem; }
h1 { font-size: 2.5rem; margin-bottom: 0.5rem; font-weight: 800; color: #0f172a; }
.subtitle { color: #64748b; font-size: 1.1rem; letter-spacing: 0.5px; }


.grid { 
  display: grid; 
  grid-template-columns: 1fr 1fr; 
  gap: 30px; 
}
.card { 
  background: var(--card-bg); 
  border-radius: 16px; 
  box-shadow: 0 10px 25px -5px rgba(0,0,0,0.08); 
  overflow: hidden; 
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  backdrop-filter: blur(10px);
}
.card:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 35px -5px rgba(0,0,0,0.12);
}
.card-header { 
  padding: 20px; 
  color: white; 
  display: flex; 
  align-items: center; 
  gap: 12px; 
}
.card-header h2 { margin: 0; font-size: 1.25rem; font-weight: 600; }
.users { background: linear-gradient(135deg, var(--primary) 0%, #818cf8 100%); }
.tickets { background: linear-gradient(135deg, var(--success) 0%, #34d399 100%); }
.card-body { padding: 30px; }


.input-group { position: relative; margin-bottom: 20px; }
input, select { 
  width: 100%; 
  padding: 12px 15px; 
  border: 1px solid #cbd5e1; 
  border-radius: 8px; 
  background: #f8fafc;
  box-sizing: border-box; 
  font-size: 1rem;
  transition: all 0.3s ease;
  outline: none;
}
input:focus, select:focus {
  background: white;
  border-color: var(--primary);
  box-shadow: 0 0 0 4px rgba(79, 70, 229, 0.1);
}

button { 
  width: 100%; 
  padding: 14px; 
  border: none; 
  border-radius: 8px; 
  color: white; 
  font-size: 1rem;
  font-weight: 600; 
  cursor: pointer; 
  transition: all 0.2s ease; 
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
button:active { transform: scale(0.97); } 

.btn-primary { background: var(--primary); }
.btn-primary:hover { background: var(--primary-hover); box-shadow: 0 6px 12px rgba(79, 70, 229, 0.3); }

.btn-success { background: var(--success); }
.btn-success:hover { background: var(--success-hover); box-shadow: 0 6px 12px rgba(16, 185, 129, 0.3); }

.btn-print { 
  background: #334155; 
  margin-top: 15px; 
}
.btn-print:hover { background: #1e293b; box-shadow: 0 6px 12px rgba(51, 65, 85, 0.3); }

.alert-box {
  margin-top: 20px;
  padding: 12px 15px;
  border-radius: 8px;
  font-weight: 500;
  text-align: center;
}
.text-success { background: #ecfdf5; color: #065f46; border: 1px solid #a7f3d0; }
.text-error { background: #fef2f2; color: #991b1b; border: 1px solid #fecaca; }


.bounce-enter-active { animation: bounce-in 0.5s; }
.bounce-leave-active { animation: bounce-in 0.5s reverse; }
@keyframes bounce-in {
  0% { transform: scale(0.9); opacity: 0; }
  50% { transform: scale(1.05); }
  100% { transform: scale(1); opacity: 1; }
}

.fade-enter-active, .fade-leave-active { transition: opacity 0.5s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; }


.fade-in-down { animation: fadeInDown 0.8s ease-out; }
.slide-up-1 { animation: slideUp 0.6s ease-out 0.2s backwards; }
.slide-up-2 { animation: slideUp 0.6s ease-out 0.4s backwards; }

@keyframes fadeInDown {
  from { opacity: 0; transform: translateY(-20px); }
  to { opacity: 1; transform: translateY(0); }
}
@keyframes slideUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 768px) { .grid { grid-template-columns: 1fr; } }

@media print {
  .no-print { display: none !important; }
  .print-only { display: block !important; }
  body { background: white; }
}
.print-only { display: none; }

.ticket-visual {
  width: 320px; padding: 25px; border: 2px dashed #1e293b;
  margin: 50px auto; font-family: 'Courier New', Courier, monospace; text-align: center;
}
.ticket-header { border-bottom: 2px solid #1e293b; padding-bottom: 15px; margin-bottom: 20px; }
.logo { font-size: 24px; font-weight: bold; }
.ticket-id { font-size: 14px; margin-top: 5px; }
.barcode { font-size: 28px; margin-top: 20px; letter-spacing: 2px; }
</style>