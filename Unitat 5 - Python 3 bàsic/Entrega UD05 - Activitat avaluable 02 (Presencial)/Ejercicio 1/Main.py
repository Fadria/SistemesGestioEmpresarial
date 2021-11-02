import re # Librería destinada al uso de expresiones regulares
from functools import reduce # Librería usada para disponer de la función reduce

# Función para valorar si un número es inferior a 10
def numerosMenores10(numero):
    if numero > 10:
          return True # Es mayor que 10, lo queremos en la lista
    return False # No es mayor que 10, será eliminado

# Función para sumar dos números
def suma(a, b):
    return a + b

lambdaMayusculas = lambda texto: texto.upper() # Función lambda que nos cambia un texto a mayúsculas
print(lambdaMayusculas("hola, esto es un texto en minúsculas")) # Lo muestra en mayúsculas


print("Introduzca sus números separados por espacios: ") # Pedimos la cadena con los números al usuario
cadenaNumeros = input()

if(re.match("[0-9 ]+",cadenaNumeros)): # Verdadero si únicamente contiene números y espacios
    listaNumeros = list(cadenaNumeros.split(" ")) # Crearemos los elementos separados por espacios
    listaNumeros = map(int, listaNumeros) # Convertimos la lista de cadenas a una lista de números
    listaNumeros = list(filter(numerosMenores10, listaNumeros)) # Aplicamos la función a nuestra variable y la guardamos como una lista

    '''
        La función reduce se encarga de realizar llamadas acumulativas de izquierda a derecha, por ello, acabaremos sumando
        cada número con el siguiente hasta finalizar la lista, sumamos el primero y el segundo y, ese resultado, luego lo sumaríamos con 
        el tecer número
    '''
    print(reduce(suma, listaNumeros))
else: # Es falso, mostraremos una excepción al contener letras
    raise Exception("Error, no se ha introducito únicamente carácteres numéricos")


