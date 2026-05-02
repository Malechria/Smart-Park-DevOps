# SmartPark - Plataforma Integral de Servicios 🎢

Bienvenido al repositorio de **SmartPark**, una plataforma basada en microservicios diseñada para gestionar la venta de boletos, usuarios y telemetría de un parque de diversiones. 

Este proyecto está construido bajo la metodología de los **12 Factores (12-Factor App)** y diseñado para ser desplegado mediante metodologías DevOps (Integración y Despliegue Continuo).

## 🏗️ Arquitectura de Microservicios
La aplicación está dividida en servicios independientes, construidos con **Python y FastAPI** para garantizar alta concurrencia y tiempos de respuesta óptimos:

1. **Servicio de Usuarios (`/servicio-usuarios`):** Gestiona la autenticación y validación de clientes.
2. **Servicio de Taquilla (`/servicio-taquilla`):** Procesa la venta de boletos y transacciones.

## 🚀 Requisitos Previos (Prerrequisitos)
Para ejecutar este proyecto en un entorno local de desarrollo (pruebas), necesitas tener instalado:
* [Docker Desktop](https://www.docker.com/products/docker-desktop/)
* [Python 3.10+](https://www.python.org/downloads/) (Solo si deseas correr el código sin contenedores)
* Git

## 🛠️ Instrucciones de Uso Local
Se utilizó Docker Compose para levantar todos los servicios simultáneamente.

1. Clona este repositorio:
   ```bash
   git clone [https://github.com/TU-USUARIO/smartpark-devops.git](https://github.com/TU-USUARIO/smartpark-devops.git)
   cd smartpark-devops