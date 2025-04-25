# Importa clases necesarias para definir columnas y tipos de datos en SQLAlchemy
from sqlalchemy import Column, Integer, String, Enum

# Importa la clase Base desde el archivo database.py (la clase que sirve como base para todos los modelos)
from database import Base

# Importa el módulo enum de Python, que permite definir enumeraciones (conjuntos limitados de valores)
import enum

# Define una enumeración llamada EstadoEnum que representa los posibles estados del usuario
# Hereda de str y enum.Enum para que sea compatible con SQLAlchemy y FastAPI
class EstadoEnum(str, enum.Enum):
    activo = "activo"
    inactivo = "inactivo"

# Define el modelo de base de datos llamado "Usuario", que representa la tabla "usuarios"
# Esta clase hereda de Base, lo que la convierte en una tabla dentro de SQLAlchemy
class Usuario(Base):
    # Nombre que tendrá la tabla en la base de datos
    __tablename__ = "usuarios"

    # Columna 'id' como clave primaria (única), tipo entero, con índice para búsquedas rápidas
    id = Column(Integer, primary_key=True, index=True)

    # Columna 'username' de tipo string (máximo 50 caracteres), no puede estar vacía, y debe ser única
    username = Column(String(50), unique=True, nullable=False)

    # Columna 'password' de tipo string (máximo 255 caracteres), no puede estar vacía
    # Se deja espacio suficiente por si usas contraseñas cifradas
    password = Column(String(255), nullable=False)

    # Columna 'estado' que utiliza el enum definido antes (activo o inactivo), con valor por defecto "activo"
    estado = Column(Enum(EstadoEnum), default=EstadoEnum.activo)
