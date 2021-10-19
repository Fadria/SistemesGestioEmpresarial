'''
    Función que recibe dos números y devuelve la suma de estos.
    Es importante definir la función antes de que esta sea invocada, ya que de lo contrario obtendríamos un error.
'''
def suma(num1, num2):
    return num1 + num2

print("La suma de 1 y 2 es: " + str(suma(1,2))) # Imprimimos el resultado de la llamada a la función

# Función que recibe una lista y la duplica
def doblarValores(lista):
    for count in range(len(lista)): # Realizaremos itineraciones desde 0 hasta el tamaño de la lista
        lista[count] = lista[count] * 2 # Guardamos el valor duplicado en la posición correspondiente de la lista

miLista = [1,2,3] # Creamos nuestra lista
print("Lista antes de duplicar: " + str(miLista)) # Mostramos sus valores
doblarValores(miLista) # Duplicamos todos los valores de la lista
print("Lista después de duplicar: " + str(miLista)) # Mostramos la lista con los valores ya duplicados