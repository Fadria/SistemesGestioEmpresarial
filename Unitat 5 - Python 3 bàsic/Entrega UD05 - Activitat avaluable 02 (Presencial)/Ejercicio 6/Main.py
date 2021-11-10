from Profesor import Profesor
from Alumno import Alumno
from Escuela import Escuela

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