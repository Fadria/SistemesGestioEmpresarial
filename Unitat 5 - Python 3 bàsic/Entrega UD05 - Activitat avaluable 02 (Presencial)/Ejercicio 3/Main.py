def numeroPatrones(texto):
    contadorCoincidencias = 0 # Contador de coincidencias de los patrones
    listaPatrones = ["00","101","ABC","HO"] # Lista de los patrones que buscamos
 
    for i in range(len(listaPatrones)): # Cada valor de la lista de patrones
        for j in range(0, len(texto)): # Desde 0 hasta el total de caracteres del texto

            '''
                Obtenemos los pedazos a comparar de la cadena, por ejemplo, de la cadena 000 tendremos los valores
                00, 00 y 0 y los buscaremos en los valores de la lista.
            '''
            cadenaAComparar = texto[j:j+len(listaPatrones[i])] 

            # Si nuestra cadena coincide con la del listado de patrones que estamos comparando aumentaremos el contador
            if cadenaAComparar == listaPatrones[i]:
                contadorCoincidencias += 1

    return contadorCoincidencias # Una vez finalizada la búsqueda devolveremos nuestro contador


print("Por favor, introduzca la cadena a comprobar: ") # Pedimos la cadena al usuario
cadena = input().upper()

# Imprimimos el resultado de la función numeroPatrones
print("El número de patrones encontrados ha sido de: " + str(numeroPatrones(cadena)))