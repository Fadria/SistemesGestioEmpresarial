import db # Importamos nuestro fichero db para usar db.Base como el padre de nuestra clase
from sqlalchemy import Column, Integer, String # Tipos de datos que usaremos en nuestra tabla
from sqlalchemy.orm import relationship # Librería usada para indicar datos relacionados con las relaciones

# Heredamos de db.Base para que nuestra base de datos funcione como un ORM
class Escuela(db.Base):

    __tablename__ = 'escuelas' # Nombre de la tabla de la base de datos
    
    id = Column(Integer, primary_key=True) # Clave primaria
    nombre = Column(String) # Campo nombre de tipo String
    localidad = Column(String) # Campo localidad de tipo String
    responsable = Column(Integer) # Campo responsable de tipo Integer
    alumnos = relationship('Alumno', backref='escuelaAlumno') # Línea usada para poder obtener los alumnos de la escuela una vez insertados
    profesores = relationship('Profesor', backref='escuelaProfesor') # Línea usada para poder obtener los profesores de la escuela una vez insertados

    # Constructor de alumno, alumnos y profesores no serán obligatorios cuando creemos el objeto
    def __init__(self, nombre, localidad, responsable):
        # Asignamos los argumentos recibidos a los atributos de la clase
        self.nombre = nombre
        self.localidad = localidad
        self.responsable = responsable

    # Actualizamos el nombre de la escuela
    def setNombre(self, nombre):
        self.nombre = nombre

    # Actualizamos la localidad de la escuela
    def setLocalidad(self, localidad):
        self.localidad = localidad

    # Actualizamos la persona responsable de la escuela
    def setResponsable(self, responsable):
        self.responsable = responsable

    # Devolvemos el nombre de la escuela
    def getNombre(self):
        return self.nombre

    # Devolvemos la localidad de la escuela
    def getLocalidad(self):
        return self.localidad

    # Devolvemos la persona responsable de la escuela
    def getResponsable(self):
        return self.responsable

    # Devolvemos los alumnos de la escuela
    def getAlumnos(self):
        return self.alumnos

    # Devolvemos los alumnos de la escuela
    def getProfesores(self):
        return self.profesores

    # Eliminamos el nombre de la escuela
    def deleteNombre(self):
        del self.nombre

    # Eliminamos la localidad de la escuela
    def deleteLocalidad(self):
        del self.localidad

    # Eliminamos la persona responsable de la escuela
    def deleteResponsable(self):
        del self.responsable

    # Añadimos un alumno
    def addAlumno(self, alumno):
        self.alumnos.append(alumno)

    # Eliminamos un alumno
    def removeAlumno(self, alumno):
        self.alumnos.remove(alumno)

    # Añadimos un profesor
    def addProfesor(self, profesor):
        if profesor.getEmpleado() == False:
            self.profesores.append(profesor)
            profesor.setEmpleado(True)
        else:
            print("El profesor indicado ya tiene una escuela asignada")

    # Eliminamos un profesor
    def removeProfesor(self, profesor):
        self.profesores.remove(profesor)
        profesor.setEmpleado(False)

    def getDatosAlumnos(self):
        cadenaAlumnos = ""
        for i in self.alumnos:
            cadenaAlumnos += i.getDatos()
        return cadenaAlumnos

    def getDatosProfesores(self):
        cadenaProfesores = ""
        for i in self.profesores:
            cadenaProfesores += i.getDatos()
        return cadenaProfesores

    # Devolvemos los datos de la escuela
    def getDatos(self):
        datosAlumnos = self.getDatosAlumnos()
        datosProfesores = self.getDatosProfesores()
        return "[Nombre: %s, Localidad: %s, Responsable: %s, Profesores: %s, Alumnos: %s]" % (self.getNombre(), self.getLocalidad(),  self.getResponsable(), datosProfesores, datosAlumnos)
