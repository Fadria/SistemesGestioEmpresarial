import db # Importamos nuestro fichero db para usar db.Base como el padre de nuestra clase
from sqlalchemy import Column, Integer, String, ForeignKey # Tipos de datos que usaremos en nuestra tabla

# Heredamos de db.Base para que nuestra base de datos funcione como un ORM
class Alumno(db.Base):
    __tablename__ = 'alumnos' # Nombre de la tabla de la base de datos
    
    id = Column(Integer, primary_key=True) # Clave primaria
    nombre = Column(String) # Campo nombre de tipo String
    curso = Column(String) # Campo curso de tipo String

    # Claves ajenas de la tabla, indicamos el nombre de ella y el campo al que la variable queda enlazado
    profesor = Column(Integer, ForeignKey('profesores.id'))
    escuela = Column(Integer, ForeignKey('escuelas.id'))

    # Constructor de alumno
    def __init__(self, nombre, curso, profesor = None, escuela = None):
        # Asignamos los argumentos recibidos a los atributos de la clase
        self.nombre = nombre
        self.curso = curso
        self.profesor = profesor
        self.escuela = escuela

    def __repr__(self):
        return f'Alumno({self.nombre}, {self.profesor}, {self.escuela})'
        
    def __str__(self):
        return self.nombre

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
