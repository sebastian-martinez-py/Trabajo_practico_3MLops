from fastapi import FastAPI
from pydantic import BaseModel

# Inicializa la aplicación FastAPI
app = FastAPI()

# Modelo de datos para recibir información en una solicitud POST
class User(BaseModel):
    name: str
    age: int
    email: str

# Ruta principal
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# Ruta dinámica que recibe un parámetro
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

# Ruta para recibir datos en un POST
@app.post("/users/")
def create_user(user: User):
    return {"message": f"User {user.name} created!", "data": user}
