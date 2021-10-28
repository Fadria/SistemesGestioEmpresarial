import random # Librería para utilizar números aleatorios

class Car(object):
    # Constructor de nuestra clase
    def __init__(self, matricula, color):
        # Asignamos los valores pasados al constructor
        self.matricula = matricula
        self.color = color
    
    # Imprimimos los datos del coche
    def imprimir(self):
        print("Matrícula: " + str(self.matricula) + " Color: " + str(self.color))

    # Devolvemos la matrícula
    def getMatricula(self):
        return self.matricula

    # Devolvemos el color
    def getColor(self):
        return self.color

# Mostramos un mensaje para indicar al usuario el dato que le vamos a pedir
print("Indique el número de instancias de la clase Car que desea crear: ")
numInstancias = int(input()) # Almacenamos el dato introducido por el usuario

listaColores = ["red", "white", "black", "pink", "blue"] # Lista de posibles colores
listaCoches = [] # Lista que guardará los coches que creemos

# Creamos de 0 coches a el número de coches introducido por el usuario
for i in range(numInstancias):
    '''
        En la primera posición aportaremos el valor de la matrícula. Como queremos comenzar en la posición 1, sumaremos 1 a i, ya que
        i comienza en el valor 0.

        En la segunda posición, enviaremos el color correspondiente a la posición generada al azar, que será desde la posición 0
        hasta la última de la lista. Restamos uno ya que nos devolvería el número total de elementos, pero el programa consideraría
        la primera posición como la 0, no como la 1.
    '''
    listaCoches.append(Car(i+1, listaColores[random.randint(0, len(listaColores)-1)]))

# Si disponemos de menos de 10 coches mostraremos los coches desde la primera posición a la del total de coches pedidos por el usuario
if len(listaCoches) < 10:
    for i in range(numInstancias):
        listaCoches[i].imprimir() # Llamamos a la función imprimir para mostrar los datos
else:
    # Si el usuario ha creado más de 10 coches, lo limitaremos a mostrar 10
    for i in range(10):
        listaCoches[i].imprimir() # Llamamos a la función imprimir para mostrar los datos