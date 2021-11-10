import db

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

# Heredamos de object para obtener una clase.
class Profesor(db.Base):
    __tablename__ = 'profesores'
    
    id = Column(Integer, primary_key=True) # ID del objeto
    nombre = Column(String, nullable=False)
    tipo = Column(String)
    alumnos = relationship('Alumno', backref='Profesor')
    escuela = relationship('Escuela', backref='Profesor')
    escuela_id = Column(Integer, ForeignKey('escuela.id'))

    # Constructor de profesor
    def __init__(self, nombre, tipo):

        # Si el sector del profesor no es uno de nuestra lista, lanzaremos una excepción
        if tipo.lower() not in ["ciencias", "letras", "otros"]:
            raise Exception("Error, el tipo de profesor no es correcto")

        # Asignamos los argumentos recibidos a los atributos de la clase
        self.nombre = nombre
        self.tipo = tipo
        self.empleado = False # Variable usada para verificar si tiene una escuela asignada

    # Actualizamos el nombre del profesor
    def setNombre(self, nombre):
        self.nombre = nombre

    # Actualizamos el tipo del profesor
    def setTipo(self, tipo):
        self.tipo = tipo

    # Indicamos un booleano según el profesor trabaje o no en una escuela
    def setEmpleado(self, empleado):
        self.empleado = empleado

    # Devolvemos el nombre del profesor
    def getNombre(self):
        return self.nombre

    # Devolvemos el tipo del profesor
    def getTipo(self):
        return self.tipo

    # Devolvemos un booleano que indica si trabaja en una escuela
    def getEmpleado(self):
        return self.empleado

    # Eliminamos el nombre del profesor
    def deleteNombre(self):
        del self.nombre

    # Eliminamos el tipo del profesor
    def deleteTipo(self):
        del self.tipo

    # Devolvemos todos los datos del profesor
    def getDatos(self):
        return "[Nombre: %s, Tipo: %s]" % (self.getNombre(), self.getTipo())