# Creamos una lista formada por listas que contienen un valor para la altura y otro para el peso
miLista = [(1.80, 75),(2.00, 90),(1.74, 80),(1.74, 75),(1.95, 80)]

print("Antes de ordenar: " + str(miLista))

'''
    Ordenamos los valores de la altura de menor a mayor, por ello, incluiremos el símbolo "-" en la posición 0.
    Y, como queremos ordenar el peso de forma ascentente, en este caso será sin usar el símbolo "-".
'''
miLista = sorted(miLista, key=lambda x: (-x[0], x[1]))

# Mostramos la lista ya ordenada
print("Después de ordenar: " + str(miLista))

'''
    PREGUNTA: Explica en comentaris que és realment la “key function”. Pista: en l’ajuda diuen
    “The value of the key parameter should be a function (or other callable) that takes a single
    argument and returns a key to use for sorting purposes. This technique is fast because the key
    function is called exactly once for each input record.”.

    RESPUESTA: La key function funcionaría de forma que, en base a unos valores, nos devuelva un
    valor que usaremos para ordenar toda nuestra lista. Por lo que necesitaríamos calcular ese
    valor para cada elemento de la lista y, finalmente, esta lista será ordenada según esos 
    valores que usa la key function.
'''