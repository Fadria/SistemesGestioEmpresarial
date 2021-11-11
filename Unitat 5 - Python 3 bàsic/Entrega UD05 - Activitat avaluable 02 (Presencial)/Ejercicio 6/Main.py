import db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from Profesor import Profesor
from Alumno import Alumno
from Escuela import Escuela


engine = create_engine('sqlite:///escuelas.sqlite') # Creamos el punto de entrada a la base de datos
Session = sessionmaker(bind=engine) # Iniciamos la transacción con la base de datos
session = Session()

p1 = Profesor(nombre='Travish', tipo='letras')
session.add( p1)
session.commit()

a1 = Alumno(nombre='Robert', curso="2DAM", profesor=p1.id)
session.add( a1 )
session.commit()


"""

p1 = Profesor("Eusebio", "otros")
a1 = Alumno("Miguel", "2DAM", p1)
e1 = Escuela("Nombre", "Localidad", "Juanjo")

p1.setNombre("Ricardo")

e1.addAlumno(a1)
e1.addProfesor(p1)
e1.addProfesor(p1)

e1.deleteNombre()
e1.setNombre("Serra Perenxisa")

print("Escuela: " + str(e1.getDatos()))
print("Alumno: " + str(a1.getDatos()))
print("Profesor: " + str(p1.getDatos()))
"""
