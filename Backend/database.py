# Importa la función create_engine para crear la conexión a la base de datos
from sqlalchemy import create_engine

# Importa herramientas para gestionar sesiones (sessionmaker) y definir modelos base (declarative_base)
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de conexión a la base de datos MySQL
# Formato: "mysql+pymysql://usuario:contraseña@host/nombre_base_datos"
# - mysql: tipo de base de datos
# - pymysql: driver que se usará para conectarse
# - usuario y contraseña: tus credenciales
# - localhost: dirección del servidor de base de datos (en este caso, local)
# - nombre_base_datos: el nombre de tu base de datos
DATABASE_URL = "mysql+pymysql://admin:crvg2489@localhost/db_user"

# Crea el motor de conexión a la base de datos usando la URL de arriba
# Este motor gestiona la conexión y se usa para ejecutar comandos en la base de datos
engine = create_engine(DATABASE_URL)

# Crea una clase SessionLocal que será usada para generar sesiones de conexión a la base de datos
# autocommit=False: no guarda automáticamente los cambios
# autoflush=False: no sincroniza automáticamente los objetos con la base de datos
# bind=engine: indica qué motor (conexión) se usará
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crea una clase base desde la cual todos los modelos de la base de datos deben heredar
# Esto es necesario para que SQLAlchemy sepa cómo mapear tus modelos (clases) a tablas en la base de datos
Base = declarative_base()
