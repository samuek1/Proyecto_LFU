from fastapi import FastAPI
from src.lfu_cache import LFUCache

app = FastAPI()
cache = LFUCache(capacity=3)

@app.get("/")
def read_root():
    return {"message": "¡API funcionando con caché LFU!"}

@app.get("/datos/{item_id}")
def get_data(item_id: int):

    cached_data = cache.get(item_id)
    if cached_data != -1:
        return {"source": "cache", "data": cached_data}


    data = {
        "id": item_id,
        "nombre": f"Elemento {item_id}",
        "descripcion": "Este es un dato de prueba desde la API."
    }


    cache.put(item_id, data)

    return {"source": "api", "data": data}