# Microservicio de Turismo y Clima

## Descripción

Este proyecto consiste en un microservicio desarrollado con FastAPI que consulta información meteorológica desde la API de Open-Meteo y genera recomendaciones de actividades turísticas según las condiciones del clima.

## Funcionalidades

- Consulta del clima actual.
- Obtención de temperatura.
- Obtención del código climático.
- Obtención de velocidad del viento.
- Recomendación de actividades turísticas.
- Regla de seguridad por fuertes vientos.
- Bloqueo de actividades al aire libre cuando el viento supera los 50 km/h.
- Generación de alerta de seguridad.

## Tecnologías utilizadas

- Python
- FastAPI
- Uvicorn
- Requests
- Open-Meteo API

## Instalación

Crear un entorno virtual:

```bash
python -m venv venv