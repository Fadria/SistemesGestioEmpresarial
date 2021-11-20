import db # Importamos nuestro fichero db para usar db.Base como el padre de nuestra clase
from sqlalchemy import Column, Integer, String, ForeignKey # Tipos de datos que usaremos en nuestra tabla
from sqlalchemy.orm import relationship # Librería usada para indicar datos relacionados con las relaciones

# Heredamos de db.Base para que nuestra base de datos funcione como un ORM
class Profesor(db.Base):

    __tablename__ = 'profesores' # Nombre de la tabla de la base de datos
    
    id = Column(Integer, primary_key=True) # Clave primaria
    nombre = Column(String) # Campo nombre de tipo String
    tipo = Column(String) # Campo tipo de tipo String
    escuela = Column(Integer, ForeignKey('escuelas.id'), nullable=True) # Clave ajena de la tabla
    alumnos = relationship('Alumno', backref='tutor') # Línea usada para poder obtener los alumnos del profesor una vez insertados

    # Constructor de profesor
    def __init__(self, nombre, tipo, escuela=None):

        # Si el sector del profesor no es uno de nuestra lista, lanzaremos una excepción
        if tipo.lower() not in ["ciencias", "letras", "otros"]:
            raise Exception("Error, el tipo de profesor no es correcto")

        # Asignamos los argumentos recibidos a los atributos de la clase
        self.nombre = nombre
        self.tipo = tipo
        self.escuela = escuela
        
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