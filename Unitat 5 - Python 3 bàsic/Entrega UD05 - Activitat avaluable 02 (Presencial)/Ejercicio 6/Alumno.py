import db

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

from Profesor import Profesor

# Heredamos de object para obtener una clase.
class Alumno(db.Base):
    __tablename__ = 'alumnos'

    id = Column(Integer, primary_key=True) # ID del objeto
    nombre = Column(String, nullable=False)
    curso = Column(String)
    escolarizado = Column(Boolean, default=False)
    profesor_id = Column( Integer, ForeignKey('profesores.id') )
    profesor = relationship( 'Profesor', back_populates='alumnos' )
        
    # Constructor de alumno
    def __init__(self, nombre, curso, profesor):
        # Asignamos los argumentos recibidos a los atributos de la clase
        self.nombre = nombre
        self.curso = curso
        self.profesor_id = profesor
        self.escolarizado = False # Variable usada para verificar si tiene una escuela asignada

    # Actualizamos el nombre del alumno
    def setNombre(self, nombre):
        self.nombre = nombre

    # Actualizamos el curso del alumno
    def setCurso(self, curso):
        self.curso = curso

    # Actualizamos el profesor del alumno
    def setProfesor(self, profesor):
        self.profesor = profesor

    # Indicamos un booleano según el estudiante estudie o no en una escuela
    def setEscolarizado(self, escolarizado):
        self.escolarizado = escolarizado

    # Devolvemos el nombre del alumno
    def getNombre(self):
        return self.nombre

    # Devolvemos el curso del alumno
    def getCurso(self):
        return self.curso

    # Devolvemos el profesor del alumno
    def getProfesor(self):
        return self.profesor

    # Devolvemos un booleano que indica si trabaja en una escuela
    def getEscolarizado(self):
        return self.escolarizado

    # Eliminamos el nombre del alumno
    def deleteNombre(self):
        del self.nombre

    # Eliminamos el curso del alumno
    def deleteCurso(self):
        del self.curso

    # Eliminamos el profesor del alumno
    def deleteProfesor(self):
        del self.profesor

    # Devolvemos todos los datos del profesor
    def getDatos(self):
        return "[Nombre: %s, Curso: %s, Profesor: %s]" % (self.getNombre(), self.getCurso(),  self.getProfesor().getDatos())
