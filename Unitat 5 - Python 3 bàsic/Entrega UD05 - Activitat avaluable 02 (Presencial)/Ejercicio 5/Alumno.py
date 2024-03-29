from Profesor import Profesor

# Heredamos de object para obtener una clase.
class Alumno(object):

    # Constructor de alumno
    def __init__(self, nombre, curso, profesor):
        # Asignamos los argumentos recibidos a los atributos de la clase
        self.nombre = nombre
        self.curso = curso
        self.profesor = profesor
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
