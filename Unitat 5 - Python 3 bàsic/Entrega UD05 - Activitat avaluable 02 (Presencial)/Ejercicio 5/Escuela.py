from Profesor import Profesor
from Alumno import Alumno

# Heredamos de object para obtener una clase.
class Escuela(object):

    # Constructor de alumno, alumnos y profesores no serán obligatorios cuando creemos el objeto
    def __init__(self, nombre, localidad, responsable, alumnos=None, profesores=None):
        # Asignamos los argumentos recibidos a los atributos de la clase
        self.nombre = nombre
        self.localidad = localidad
        self.responsable = responsable
        self.alumnos = []
        self.profesores = []

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
