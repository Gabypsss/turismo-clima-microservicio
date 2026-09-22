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


def aplicar_regla_seguridad(viento, recomendaciones):
    actividades_exteriores = [
        "Caminata turística",
        "Visitar un parque",
        "Recorrido en bicicleta",
        "Recorrido por la ciudad",
        "Visitar un mirador"
    ]

    if viento > 50:
        recomendaciones_seguras = [
            actividad
            for actividad in recomendaciones
            if actividad not in actividades_exteriores
        ]

        return {
            "alerta_seguridad": True,
            "mensaje": "Alerta de seguridad: viento superior a 50 km/h. Se bloquearon las actividades al aire libre.",
            "recomendaciones": recomendaciones_seguras
        }

    return {
        "alerta_seguridad": False,
        "mensaje": "Condiciones de viento dentro del rango permitido.",
        "recomendaciones": recomendaciones
    }


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

    resultado_seguridad = aplicar_regla_seguridad(
    clima_actual["wind_speed_10m"],
    recomendaciones
    )       


    return {
        "ciudad": "Bogotá",
        "temperatura": clima_actual["temperature_2m"],
        "codigo_clima": clima_actual["weather_code"],
        "velocidad_viento": clima_actual["wind_speed_10m"],
        "alerta_seguridad": resultado_seguridad["alerta_seguridad"],
        "mensaje": resultado_seguridad["mensaje"],
        "recomendaciones": resultado_seguridad["recomendaciones"]
    }
@app.get("/prueba-seguridad")
def prueba_seguridad(viento: float):
    recomendaciones = [
        "Caminata turística",
        "Visitar un parque",
        "Recorrido en bicicleta"
    ]

    resultado = aplicar_regla_seguridad(
        viento,
        recomendaciones
    )

    return {
        "velocidad_viento": viento,
        "alerta_seguridad": resultado["alerta_seguridad"],
        "mensaje": resultado["mensaje"],
        "recomendaciones": resultado["recomendaciones"]
    }