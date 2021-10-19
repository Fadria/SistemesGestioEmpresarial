# Lista original
listaOriginal = ["Antonio", "José", "María", "Elisa", "Diego", "Ricardo", "Maria José", "Eduardo", "Miguel"]

'''
    Al copiar una lista, comenzaremos a copiar desde la posición que indiquemos a la izquierda del símbolo ":" y
    finalizaremos la copia en la posición que indiquemos a la derecha.

    Como podemos ver, nosotros no indicamos valores, esto hará que por defecto copiemos desde el principio hasta el final de la lista.
'''
listaCopiada = listaOriginal[:]

# Pregunta: ¿Cuál es la diferencia en Python entre "shallow copy" y "deep copy"?
'''
    La diferencia entre estos dos tipos de copia radica en que cuando usamos shallow copy haremos una copia con las referencias a
    los valores del array que copiamos. Es decir, si eliminamos un valor en el array original, con shallow copy también lo perderíamos.

    Sin embargo, con deep copy, no usaríamos referencias. Esos valores serían copiados en su totalidad.
'''

# Eliminamos un elemento de la lista original y añadimos uno a la copiada
listaOriginal.pop()
listaCopiada.append("Juanjo")

# Mostramos los valores para comprobar que disponemos de datos diferentes
print("Lista original: " + str(listaOriginal))
print("Lista copiada: " + str(listaCopiada))

# Creamos una lista nueva con los últimos 4 elementos de la lista copiada y la imprimimos
lista4Elementos = listaCopiada[-4:]
print("Lista con 4 elementos: " + str(lista4Elementos))

# Creamos una lista a partir de las palabras de una cadena y la imprimimos
listaPalabras = list("Estas palabras están separadas por un espacio".split(" "))
print("Lista creada a partir de ua cadena: " + str(listaPalabras))