from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
def inicio():
    return {
        "mensaje": "Microservicio de turismo y clima funcionando"
    }


@app.get("/clima")
def obtener_clima():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=4.7110"
        "&longitude=-74.0721"
        "&current=temperature_2m,weather_code,wind_speed_10m"
        "&wind_speed_unit=kmh"
    )

    respuesta = requests.get(url)
    datos = respuesta.json()

    clima_actual = datos["current"]

    return {
        "ciudad": "Bogotá",
        "temperatura": clima_actual["temperature_2m"],
        "codigo_clima": clima_actual["weather_code"],
        "velocidad_viento": clima_actual["wind_speed_10m"]
    }
def recomendar_actividades(codigo_clima):
    if codigo_clima == 0:
        return [
            "Caminata turística",
            "Visitar un parque",
            "Recorrido en bicicleta"
        ]

    elif codigo_clima in [1, 2, 3]:
        return [
            "Recorrido por la ciudad",
            "Visitar un mirador",
            "Caminata turística"
        ]

    else:
        return [
            "Visitar un museo",
            "Ir a un centro cultural",
            "Actividad gastronómica"
        ]
@app.get("/recomendaciones")
def obtener_recomendaciones():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=4.7110"
        "&longitude=-74.0721"
        "&current=temperature_2m,weather_code,wind_speed_10m"
        "&wind_speed_unit=kmh"
    )

    respuesta = requests.get(url)
    datos = respuesta.json()

    clima_actual = datos["current"]

    recomendaciones = recomendar_actividades(
        clima_actual["weather_code"]
    )

    return {
        "ciudad": "Bogotá",
        "temperatura": clima_actual["temperature_2m"],
        "codigo_clima": clima_actual["weather_code"],
        "velocidad_viento": clima_actual["wind_speed_10m"],
        "recomendaciones": recomendaciones
    }