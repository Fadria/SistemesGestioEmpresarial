import sys

def esPalindromo(numero):
    if len(numero) == 1:
        return 1 # Al ser un único número se lee igual de izquierda a derecha
    
    if len(numero) % 2 == 0: # Si es un número par trabajaremos de la siguiente forma
        numerosHastaMitad = int(len(numero)/2) # Almacenamos la mitad de la longitud para comparar las mitades
        ultimaPosicion = len(numero) -1 # Almacenamos la última posición. -1 al trabajar desde la posición 0 a la última -1

        for i in range(numerosHastaMitad): # Recorremos el bucle hasta la mitad
            '''
                En este if, comparamos una posición de una mitad con la correspondiente de la otra mitad.
                Por ejemplo, en el número 1234 compararíamos 1[posición 0] con 4[longitud del número -0] 
                y luego 2[posición 1] con 3[longitud del número -1].
            '''
            if numero[i] != numero[ultimaPosicion-i]:
                return 0 # No se cumple la condición, descartamos que sea un palíndromo
    else: # Tratamos con un número impar
        print(numero)
        print(len(numero))
        return 1

    return 1
    
def esPrimo(numero):
    return 1

numPalindromos = 0
numPrimos = 0
numPalindromosPrimos = 0

# Creamos una variable para el fichero de entrada y otra para el fichero de salida
ficheroEntrada=sys.argv[1]
ficheroSalida=sys.argv[2]

esPalindromo("121")

"""
fichero = open(ficheroEntrada) # Abrimos el fichero que contiene los números
for numero in fichero:
    numero = numero.replace("\n", "") # Eliminamos los saltos de línea

    palindromo = esPalindromo(numero) # Llamamos a la función esPalindromo y guardamos su respuesta
    numPalindromos += palindromo # Aumentamos su valor si es palindromo. 1 = palindromo, 0 = no palindromo

    primo = esPrimo(numero) # Llamamos a la funcion esPrimo y guardamos su respuesta
    numPrimos += primo # Aumentamos su valor si es primo. 1 = primo, 0 = no primo

    if palindromo == 1 and primo == 1:
        numPalindromosPrimos += 1
"""
