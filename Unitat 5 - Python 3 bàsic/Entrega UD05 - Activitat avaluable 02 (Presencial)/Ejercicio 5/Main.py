from Profesor import Profesor
from Alumno import Alumno
from Escuela import Escuela

p1 = Profesor("Eusebio", "otros")
a1 = Alumno("Miguel", "2DAM", p1)
e1 = Escuela("Nombre", "Localidad", "Juanjo")
e1.addAlumno(a1)
e1.addProfesor(p1)
print(e1.getDatos())
