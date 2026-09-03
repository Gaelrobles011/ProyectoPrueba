from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Configuración de CORS para que tu app en Reflex pueda consultarla sin problemas
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Catálogo centralizado de tu tienda (puedes reemplazarlo por una base de datos real)
INVENTARIO_TIENDA = [
    {"id": 1, "nombre": "Xiaomi POCO F6 Pro", "categoria": "Celulares", "precio": "$9,999 MXN", "stock": 5},
    {"id": 2, "nombre": "Spider-Man 2 (PS5)", "categoria": "Videojuegos", "precio": "$1,399 MXN", "stock": 10},
    {"id": 3, "nombre": "Chainsaw Man", "categoria": "Mangas", "precio": "$159 MXN", "stock": 20},
    {"id": 4, "nombre": "Watchmen", "categoria": "Cómics", "precio": "$450 MXN", "stock": 8}
]

@app.get("/api/productos")
def obtener_productos(q: str = ""):
    """Endpoint que filtra los productos según lo que busque el usuario."""
    if not q:
        return {"resultados": INVENTARIO_TIENDA}
    
    resultados = [
        item for item in INVENTARIO_TIENDA 
        if q.lower() in item["nombre"].lower() or q.lower() in item["categoria"].lower()
    ]
    
    if resultados:
        return {"resultados": resultados}
    return {"resultados": [], "mensaje": "Lo siento, no encontré ese producto en el inventario."}