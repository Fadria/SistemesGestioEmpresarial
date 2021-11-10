import db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///escuelas.sqlite') # Creamos el punto de entrada a la base de datos
Session = sessionmaker(bind=engine) # Iniciamos la transacción con la base de datos
session = Session()

Base = declarative_base() # Realiza el mapeo a partir de los modelos

def run():
    pass

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    run()