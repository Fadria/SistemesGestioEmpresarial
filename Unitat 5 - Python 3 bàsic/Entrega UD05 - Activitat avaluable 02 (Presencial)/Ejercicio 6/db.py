from sqlalchemy import create_engine # Librería del engine, punto de acceso a la base de datos
from sqlalchemy.ext.declarative import declarative_base # Clase de la que heredan todas las que usaremos para poder funcionar como un ORM
from sqlalchemy.orm import sessionmaker # Librería para crear una sesión/transacción de datos

engine = create_engine('sqlite:///escuelas.sqlite') # Variable que contiene el engine de la base de datos escuelas
Session = sessionmaker(bind=engine) # Variable que contiene nuestra sesión
session = Session() # Iniciamos la sesión

Base = declarative_base() # Variable que asignaremos como el padre de nuestras diferentes clases