# Proyecto: API Cliente con Caché LFU usando FastAPI

## Descripción

Este proyecto es una **API RESTful** desarrollada en **FastAPI**, que permite consultar información de usuarios desde una API externa (https://jsonplaceholder.typicode.com/) y utiliza un sistema de **caché LFU (Least Frequently Used)** para optimizar las respuestas.  
El sistema de caché almacena las consultas más frecuentes y descarta las menos usadas cuando se alcanza el límite de almacenamiento.

## Características principales

- Consulta de usuarios a través de un endpoint REST.
- Caché inteligente con algoritmo **LFU** para reducir peticiones externas.
- Respuesta rápida gracias al sistema de caché.
- Manejo de errores para usuarios no encontrados.
- Desarrollado en **FastAPI**, con tipado fuerte y documentación automática.

## Estructura del Proyecto

```
.
├── src
│   ├── api_client.py    # Archivo principal donde está la API
│   ├── lfu_cache.py     # Implementación del algoritmo LFU
│
├── .venv/               # Entorno virtual (no se sube a repositorios)
├── requirements.txt    # Librerías necesarias
└── README.md           # Este archivo
```

## Instalación y Ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

### 2. Crear entorno virtual
```bash
python -m venv .venv
```

### 3. Activar entorno virtual

- **Windows:**
```bash
.venv\Scripts\activate
```

- **Linux / MacOS:**
```bash
source .venv/bin/activate
```

### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 5. Ejecutar el servidor
```bash
uvicorn src.api_client:app --reload
```

## 🔗 Uso de la API

### Consultar usuario por ID

**Método:** `GET`  
**Endpoint:** `/users/{user_id}`  

**Ejemplo:**
```bash
GET http://127.0.0.1:8000/users/1
```

**Respuesta exitosa:**
```json
{
  "id": 1,
  "name": "Leanne Graham",
  "username": "Bret",
  "email": "Sincere@april.biz"
}
```

**Respuesta si no se encuentra el usuario:**
```json
{
  "detail": "User not found"
}
```

## Funcionamiento del Caché LFU

- Cada vez que se consulta un usuario, si está en caché, se devuelve rápidamente.
- Si no está en caché, se consulta la API externa y se guarda en caché.
- Cuando el caché está lleno, elimina el usuario menos consultado (menor frecuencia de uso).

## Tecnologías usadas

- **FastAPI**
- **HTTPX**
- **Python 3.10+**

## Autores 

- **Juan José Cuervo Osorio**

- **Samuel Gutierrez**

- **Alejadra Estrada Ochoa**
---
