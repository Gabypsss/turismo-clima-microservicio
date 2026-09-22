# Microservicio de Turismo y Clima

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un microservicio orientado al sector turismo, cuyo objetivo es consultar información meteorológica en tiempo real y generar recomendaciones de actividades para los viajeros de acuerdo con las condiciones del clima.

El microservicio fue desarrollado utilizando **Python** y **FastAPI**, y consume información meteorológica desde la API pública de **Open-Meteo**.

Durante el desarrollo se presentó un cambio importante en los requerimientos del cliente. Inicialmente, las recomendaciones se generaban únicamente con base en las condiciones generales del clima.

Posteriormente, se solicitó incorporar una regla de seguridad relacionada con la velocidad del viento.

La nueva condición establece que cuando la velocidad del viento supere los **50 km/h**, el sistema debe bloquear las recomendaciones correspondientes a actividades al aire libre y generar una alerta de seguridad.

---

# Problema planteado

Una empresa de turismo requiere un microservicio capaz de consultar las condiciones climáticas de un destino y recomendar actividades apropiadas para los viajeros.

La solución debe consumir una API externa de clima y utilizar los datos obtenidos para generar recomendaciones.

Durante el desarrollo, el cliente introduce el siguiente cambio crítico:

> Si la velocidad del viento supera los 50 km/h, el sistema debe bloquear automáticamente todas las recomendaciones al aire libre, sin importar si está soleado, y debe generar una alerta de seguridad.

Este cambio obliga al sistema a priorizar la seguridad del viajero sobre las recomendaciones generadas únicamente a partir del estado general del clima.

---

# Objetivo general

Desarrollar un microservicio que consulte información meteorológica y genere recomendaciones turísticas dinámicas, incorporando una regla de seguridad que restrinja actividades al aire libre cuando la velocidad del viento supere los 50 km/h.

---

# Objetivos específicos

- Consumir una API externa de información meteorológica.
- Obtener temperatura, código del clima y velocidad del viento.
- Generar recomendaciones turísticas según el clima.
- Incorporar una regla de seguridad asociada a la velocidad del viento.
- Bloquear actividades al aire libre cuando el viento supere los 50 km/h.
- Generar una alerta de seguridad.
- Exponer la funcionalidad mediante endpoints REST.
- Documentar los endpoints mediante Swagger.
- Implementar pruebas unitarias.
- Implementar pruebas manuales para los valores límite.
- Gestionar el código fuente mediante Git y GitHub.

---

# Tecnologías utilizadas

El proyecto utiliza las siguientes tecnologías:

- **Python**
- **FastAPI**
- **Uvicorn**
- **Requests**
- **Open-Meteo API**
- **Git**
- **GitHub**
- **Swagger UI**
- **Unittest**

---

# Arquitectura general

El funcionamiento del sistema puede representarse de la siguiente manera:

```text
Usuario
   |
   v
Microservicio FastAPI
   |
   v
Consulta a Open-Meteo
   |
   v
Obtención de datos meteorológicos
   |
   v
Generación de recomendaciones
   |
   v
Evaluación de la regla de seguridad
   |
   v
Respuesta al usuario
```

---

# Flujo de funcionamiento

El flujo general del microservicio es el siguiente:

1. El usuario realiza una solicitud.
2. El microservicio consulta la API de Open-Meteo.
3. Se obtienen datos como temperatura, código climático y velocidad del viento.
4. El sistema genera recomendaciones según el estado del clima.
5. Se evalúa la velocidad del viento.
6. Si el viento supera los 50 km/h:
   - Se activa una alerta de seguridad.
   - Se eliminan las actividades al aire libre.
7. Si el viento es igual o inferior a 50 km/h:
   - No se activa la alerta.
   - Las recomendaciones se mantienen.
8. El sistema devuelve la respuesta en formato JSON.

---

# Estructura del proyecto

```text
turismo-clima-microservicio/
│
├── main.py
├── test_main.py
├── requirements.txt
├── README.md
├── .gitignore
└── venv/
```

La carpeta `venv` corresponde al entorno virtual de Python y no se almacena en GitHub gracias al archivo `.gitignore`.

---

# Descripción de archivos

## main.py

Es el archivo principal del microservicio.

Contiene:

- Inicialización de FastAPI.
- Endpoint principal.
- Consulta del clima.
- Generación de recomendaciones.
- Regla de seguridad.
- Endpoint de recomendaciones.
- Endpoint de prueba de seguridad.

---

## test_main.py

Contiene las pruebas unitarias de la regla de seguridad.

Se prueban tres escenarios principales:

```text
49 km/h
50 km/h
51 km/h
```

---

## requirements.txt

Contiene las dependencias necesarias para ejecutar el proyecto.

Se pueden instalar mediante:

```bash
pip install -r requirements.txt
```

---

## .gitignore

Permite excluir archivos y carpetas que no deben subirse al repositorio.

Ejemplo:

```text
venv/
__pycache__/
*.pyc
```

---

# API meteorológica utilizada

El proyecto utiliza **Open-Meteo** como fuente de información meteorológica.

Se consultan los siguientes datos:

```text
temperature_2m
weather_code
wind_speed_10m
```

Actualmente el ejemplo utiliza coordenadas correspondientes a Bogotá:

```text
Latitud: 4.7110
Longitud: -74.0721
```

---

# Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/Gabypsss/turismo-clima-microservicio.git
```

Entrar a la carpeta:

```bash
cd turismo-clima-microservicio
```

---

## 2. Crear el entorno virtual

```bash
python -m venv venv
```

---

## 3. Activar el entorno virtual en Windows

En PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Luego:

```powershell
.\venv\Scripts\Activate.ps1
```

Cuando el entorno esté activo debería aparecer:

```text
(venv)
```

al inicio de la terminal.

---

## 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

---

# Ejecución

Ejecutar el microservicio mediante:

```bash
uvicorn main:app --reload
```

El servidor estará disponible en:

```text
http://127.0.0.1:8000
```

---

# Endpoints disponibles

## 1. Endpoint principal

```http
GET /
```

Permite comprobar que el microservicio está funcionando.

Ejemplo de respuesta:

```json
{
  "mensaje": "Microservicio de turismo y clima funcionando"
}
```

---

## 2. Endpoint de clima

```http
GET /clima
```

Consulta información meteorológica desde Open-Meteo.

Ejemplo:

```json
{
  "ciudad": "Bogotá",
  "temperatura": 13.5,
  "codigo_clima": 1,
  "velocidad_viento": 2.9
}
```

Los valores pueden variar porque corresponden a datos meteorológicos reales.

---

## 3. Endpoint de recomendaciones

```http
GET /recomendaciones
```

Este endpoint genera recomendaciones turísticas y aplica la regla de seguridad.

Ejemplo:

```json
{
  "ciudad": "Bogotá",
  "temperatura": 13.5,
  "codigo_clima": 1,
  "velocidad_viento": 2.9,
  "alerta_seguridad": false,
  "mensaje": "Condiciones de viento dentro del rango permitido.",
  "recomendaciones": [
    "Recorrido por la ciudad",
    "Visitar un mirador",
    "Caminata turística"
  ]
}
```

---

## 4. Endpoint de prueba de seguridad

```http
GET /prueba-seguridad?viento=51
```

Este endpoint permite probar manualmente la regla de seguridad sin depender de la velocidad real del viento obtenida desde Open-Meteo.

Esto facilita demostrar el comportamiento del sistema durante la exposición.

---

# Lógica de recomendaciones

## Clima despejado

Cuando el código climático es:

```text
0
```

el sistema puede recomendar:

```text
Caminata turística
Visitar un parque
Recorrido en bicicleta
```

---

## Clima parcialmente nublado

Cuando el código climático corresponde a:

```text
1
2
3
```

el sistema puede recomendar:

```text
Recorrido por la ciudad
Visitar un mirador
Caminata turística
```

---

## Otras condiciones climáticas

Para otros códigos, se recomiendan actividades bajo techo:

```text
Visitar un museo
Ir a un centro cultural
Actividad gastronómica
```

---

# Cambio solicitado por el cliente

Durante el desarrollo se recibió el siguiente cambio:

> Si la velocidad del viento supera los 50 km/h, el sistema debe bloquear automáticamente todas las recomendaciones al aire libre, sin importar si está soleado, y generar una alerta de seguridad.

La seguridad pasa a tener prioridad sobre el estado general del clima.

---

# Regla de seguridad

La condición implementada es:

```python
if viento > 50:
```

Esto significa:

```text
49 km/h  -> No activa alerta
50 km/h  -> No activa alerta
51 km/h  -> Activa alerta
```

El valor exacto de 50 km/h no activa la condición porque el requerimiento especifica que el viento debe **superar** los 50 km/h.

---

# Actividades consideradas al aire libre

Las siguientes actividades se consideran exteriores:

```text
Caminata turística
Visitar un parque
Recorrido en bicicleta
Recorrido por la ciudad
Visitar un mirador
```

Cuando la regla de seguridad se activa, estas actividades son eliminadas de la respuesta.

---

# Pruebas manuales del endpoint de seguridad

El endpoint `/prueba-seguridad` permite probar directamente diferentes velocidades de viento.

## Prueba 1: viento de 49 km/h

Abrir:

```text
http://127.0.0.1:8000/prueba-seguridad?viento=49
```

Resultado esperado:

```json
{
  "velocidad_viento": 49.0,
  "alerta_seguridad": false,
  "mensaje": "Condiciones de viento dentro del rango permitido.",
  "recomendaciones": [
    "Caminata turística",
    "Visitar un parque",
    "Recorrido en bicicleta"
  ]
}
```

Interpretación:

```text
No se activa la alerta.
Las actividades al aire libre continúan permitidas.
```

---

## Prueba 2: viento de 50 km/h

Abrir:

```text
http://127.0.0.1:8000/prueba-seguridad?viento=50
```

Resultado esperado:

```json
{
  "velocidad_viento": 50.0,
  "alerta_seguridad": false,
  "mensaje": "Condiciones de viento dentro del rango permitido.",
  "recomendaciones": [
    "Caminata turística",
    "Visitar un parque",
    "Recorrido en bicicleta"
  ]
}
```

Interpretación:

```text
No se activa la alerta.
El requerimiento indica "supera los 50 km/h".
Por lo tanto, 50 km/h todavía se considera permitido.
```

---

## Prueba 3: viento de 51 km/h

Abrir:

```text
http://127.0.0.1:8000/prueba-seguridad?viento=51
```

Resultado esperado:

```json
{
  "velocidad_viento": 51.0,
  "alerta_seguridad": true,
  "mensaje": "Alerta de seguridad: viento superior a 50 km/h. Se bloquearon las actividades al aire libre.",
  "recomendaciones": []
}
```

Interpretación:

```text
Se activa la alerta de seguridad.
Las actividades al aire libre quedan bloqueadas.
```

---

# Tabla resumen de pruebas

| Velocidad del viento | Alerta | Actividades exteriores |
|---|---|---|
| 49 km/h | No | Permitidas |
| 50 km/h | No | Permitidas |
| 51 km/h | Sí | Bloqueadas |

---

# Pruebas unitarias

Además de las pruebas manuales, el proyecto incluye pruebas unitarias utilizando `unittest`.

Para ejecutarlas:

```bash
python -m unittest test_main.py
```

Si todo funciona correctamente, debe aparecer una salida similar a:

```text
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

---

# Casos validados mediante pruebas unitarias

## Caso 1

```text
Viento: 49 km/h
Resultado esperado: alerta false
```

## Caso 2

```text
Viento: 50 km/h
Resultado esperado: alerta false
```

## Caso 3

```text
Viento: 51 km/h
Resultado esperado: alerta true
```

Estas pruebas permiten verificar automáticamente que la regla se mantiene funcionando después de realizar cambios en el código.

---

# Swagger

FastAPI genera automáticamente documentación interactiva.

Se puede acceder desde:

```text
http://127.0.0.1:8000/docs
```

Desde Swagger es posible visualizar y ejecutar:

```text
GET /
GET /clima
GET /recomendaciones
GET /prueba-seguridad
```

Esto permite probar el microservicio directamente desde el navegador.

---

# Gestión del cambio

Uno de los objetivos principales del ejercicio es demostrar cómo el sistema responde ante un cambio de requerimientos realizado durante el desarrollo.

La versión inicial únicamente generaba recomendaciones según el clima.

Posteriormente se agregó la regla de seguridad por viento.

Para evitar modificar toda la aplicación, la validación se implementó mediante una función específica:

```python
aplicar_regla_seguridad()
```

De esta manera se mantienen separadas las responsabilidades de:

```text
Consulta meteorológica
Generación de recomendaciones
Validación de seguridad
```

---

# Impacto técnico del cambio

El nuevo requerimiento afectó principalmente la lógica de negocio.

Fue necesario:

- Evaluar la velocidad del viento.
- Crear una regla específica de seguridad.
- Identificar cuáles actividades se realizan al aire libre.
- Bloquear estas actividades cuando corresponde.
- Incorporar un mensaje de alerta.
- Modificar el endpoint de recomendaciones.
- Crear un endpoint de prueba.
- Implementar pruebas unitarias.
- Actualizar la documentación.

No fue necesario reconstruir completamente el microservicio ni cambiar la integración con Open-Meteo.

---

# Resultado del cambio

La solución final permite:

- Consultar el clima real.
- Generar recomendaciones turísticas.
- Detectar condiciones de viento fuerte.
- Priorizar la seguridad del usuario.
- Bloquear actividades al aire libre.
- Mostrar alertas.
- Probar manualmente diferentes velocidades.
- Ejecutar pruebas unitarias.
- Registrar los cambios mediante Git.

---

# Beneficios de la solución

- Mayor seguridad para el viajero.
- Separación de responsabilidades.
- Mayor facilidad de mantenimiento.
- Adaptación a cambios de requerimientos.
- Posibilidad de incorporar nuevas reglas.
- Pruebas automáticas.
- Documentación interactiva.
- Control de versiones.

---

# Posibles mejoras futuras

El proyecto podría ampliarse con:

- Selección dinámica de ciudad.
- Geolocalización automática.
- Pronóstico de varios días.
- Reglas por lluvia fuerte.
- Alertas por tormentas.
- Reglas por temperaturas extremas.
- Calidad del aire.
- Base de datos de actividades.
- Clasificación de actividades por ciudad.
- Interfaz web.
- Aplicación móvil.
- Sistema de usuarios.
- Notificaciones automáticas.

---

# Historial del desarrollo

El repositorio conserva el historial de cambios mediante Git.

Entre los commits principales pueden encontrarse:

```text
Version inicial del microservicio con recomendaciones segun clima
```

```text
Agrega regla de seguridad por viento superior a 50 kmh
```

```text
Agrega documentacion y dependencias del proyecto
```

```text
Agrega pruebas para regla de seguridad por viento
```

```text
Agrega endpoint para pruebas de seguridad por viento
```

```text
Documenta endpoint de prueba de seguridad
```

Esto permite observar claramente la evolución de la solución.

---

# Control de versiones

Git se utiliza para:

- Registrar cambios.
- Mantener un historial del desarrollo.
- Identificar el momento en que se implementó el cambio crítico.
- Facilitar el trabajo colaborativo.
- Recuperar versiones anteriores.
- Compartir el proyecto mediante GitHub.

---

# Trabajo colaborativo

El repositorio puede ser desarrollado por los tres integrantes del equipo.

Cada integrante puede:

- Clonar el repositorio.
- Realizar cambios.
- Crear commits.
- Subir cambios.
- Crear ramas.
- Revisar el historial.

Esto permite evidenciar el trabajo realizado por cada miembro.

---

# Repositorio

Repositorio del proyecto:

```text
https://github.com/Gabypsss/turismo-clima-microservicio
```

---

# Integrantes

```text
Integrante 1: Gabriela Puentes Saray
Integrante 2: Juan Camilo Arias Suarez
Integrante 3: Mariana Hurtado Ducuara
Integrante 4: Heiler David Abadia Florez
```

---

# Conclusión

El microservicio desarrollado permite consumir información meteorológica desde una API externa y utilizarla para generar recomendaciones turísticas.

El cambio solicitado por el cliente permitió incorporar una regla adicional de seguridad asociada a la velocidad del viento.

La solución fue implementada sin reconstruir completamente el sistema, separando la validación de seguridad de la lógica de recomendaciones.

Las pruebas con 49, 50 y 51 km/h permiten demostrar claramente que el comportamiento del sistema coincide con el requerimiento solicitado.

Además, el uso de Git, GitHub, pruebas unitarias y Swagger permite mantener el proyecto documentado, verificable y preparado para futuras modificaciones.