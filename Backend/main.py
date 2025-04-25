# Importa FastAPI para crear la API, y Depends para manejar dependencias (como la conexión a la base de datos)
from fastapi import FastAPI, Depends

# Importa la clase Session de SQLAlchemy, que se usa para interactuar con la base de datos
from sqlalchemy.orm import Session

# Importa las herramientas necesarias para crear la base de datos y sesiones
# - SessionLocal: función para obtener una sesión de base de datos
# - engine: motor de conexión
# - Base: clase base para crear las tablas con SQLAlchemy
from database import SessionLocal, engine, Base

# Importa el modelo Usuario, que representa la tabla 'usuarios'
from models import Usuario

# Crea una instancia de la aplicación FastAPI
app = FastAPI()

# Crea todas las tablas definidas en los modelos si aún no existen
# En este caso, creará la tabla 'usuarios' según el modelo Usuario
Base.metadata.create_all(bind=engine)

# Dependencia que se usará para obtener una sesión de base de datos en los endpoints
# Esto permite abrir una sesión antes de cada petición y cerrarla automáticamente después
def get_db():
    db = SessionLocal()  # Crea una sesión
    try:
        yield db          # Devuelve la sesión para usarla en los endpoints
    finally:
        db.close()        # Cierra la sesión cuando se termina la petición

# Define una ruta GET en la raíz ("/")
# Cuando el usuario accede a http://localhost:8000/, verá este mensaje
@app.get("/")
def read_root():
    return {"mensaje": "API conectada a MySQL 😎"}
