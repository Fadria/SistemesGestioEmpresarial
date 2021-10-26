# Creación de las variables usadas en el ejercicio
lista1 = ["Docker", "Odoo", "Python"]
lista2 = lista1
lista3 = lista1[:]

'''
    Con el operador is comprobamos si los dos objetos indicados corresponden al mismo objeto,
    no a si sus valores son iguales
'''

print("Ejemplo del operando IS")
print("Lista 1 y lista 2 -> " + str(lista1 is lista2)) # True - Mismo objeto
print("Lista 1 y lista 3 -> " + str(lista1 is lista3)) # False - No son el mismo objeto
print("Lista 2 y lista 3 -> " + str(lista2 is lista3) + "\n\n") # False - No son el mismo objeto

# Con el operador NOT comprobamos si algo no es cierto
print("Ejemplo del operando NOT")
print("¿1 no es igual a 2? -> " + str(not(1 == 2))); # True - 1 y 2 no son iguales, es cierto
print("¿1 no es igual a 1? -> " + str(not(1 == 1)) + "\n\n"); # False - 1 y 1 son iguales, es falso

# Con el operador IN comprobamos si un valor se encuentra dentro de una lista
print("Ejemplo del operando IN")
if "PHP" in lista1:
    print("PHP está dentro del listado con los valores" + str(lista1))
else:
    print("PHP no está dentro del listado con los valores " + str(lista1))

if "Odoo" in lista1:
    print("Odoo está dentro del listado con los valores" + str(lista1))
else:
    print("Odoo no está dentro del listado con los valores " + str(lista1))