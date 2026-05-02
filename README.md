## SmartPark - Sistema Integral de Gestión y Taquilla
Descripción del Proyecto
Este repositorio contiene el código fuente, la configuración de infraestructura y las canalizaciones de despliegue para SmartPark. Es una aplicación basada en una arquitectura de microservicios, diseñada bajo la metodología de los 12 factores (12-Factor App), para gestionar el registro de visitantes y la emisión automatizada de boletos en un parque de diversiones.

El objetivo principal de este repositorio es demostrar la implementación integral de la filosofía y ciclo de vida DevOps. Abarca desde el desarrollo local y la contenedorización, hasta el aprovisionamiento de infraestructura en la nube, la orquestación, la automatización CI/CD y la observabilidad.

## Arquitectura y Tecnologías Utilizadas
Desarrollo y Contenedorización (Fase 1)
Frontend: Vue.js 3, Vite, Axios.

Backend (Microservicios): Python 3, FastAPI, SQLAlchemy, Pydantic.

Base de Datos: PostgreSQL.

Contenedores: Docker, Docker Compose.

## Infraestructura y Gestión de Configuración (Fase 2)
Infraestructura como Código (IaC): Terraform (Aprovisionamiento de recursos AWS EC2, VPC).

Gestión de Configuración: Ansible.

Seguridad: HashiCorp Vault (Diseño y documentación de gestión de secretos).

## Orquestación, CI/CD y Monitoreo (Fase 3)
Orquestación de Contenedores: Kubernetes, gestionado mediante AWS EKS.

Empaquetado de Aplicaciones: Helm Charts.

Integración y Entrega Continua (CI/CD): GitHub Actions.

Observabilidad: Prometheus (Recolección de métricas de series temporales) y Grafana (Visualización y dashboards).

## Requisitos Previos
Para ejecutar este proyecto en un entorno local, es necesario contar con el siguiente software instalado:

Docker

Docker Compose

Git

## Ejecución en Entorno Local
Clonar el repositorio:
git clone https://github.com/TU_USUARIO/Smart-Park-DevOps.git
cd Smart-Park-DevOps

## Construir y levantar los contenedores en segundo plano:
docker-compose up -d --build

## Acceder a los servicios a través del navegador:
Portal Web (Frontend): http://localhost:5173

API Usuarios (Swagger UI): http://localhost:8001/docs

API Taquilla (Swagger UI): http://localhost:8002/docs

## Para detener y eliminar los recursos locales de manera segura preservando los volúmenes de datos:
docker-compose down

## Flujo de Trabajo CI/CD
El proyecto cuenta con un flujo de trabajo automatizado configurado en `.github/workflows/ci-cd.yml`. Cada vez que se realiza un `push` a la rama `main`, el pipeline ejecuta los siguientes pasos:
1.  Descarga del código fuente.
2.  Configuración del entorno (Python, Node.js).
3.  Construcción (Build) de las imágenes de Docker para cada microservicio y el frontend.
4.  Validación de empaquetado con Helm.
