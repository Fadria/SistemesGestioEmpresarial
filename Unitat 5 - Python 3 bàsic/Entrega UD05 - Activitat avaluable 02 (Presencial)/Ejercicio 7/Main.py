import sys # Librería usada para leer los datos enviados por el usuario desde la terminal al ejecutar el fichero .py

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
        # Si es un número impar, restaremos uno, es decir, el número central no nos importará y calcularemos cuál es su mitad
        numerosHastaMitad = int((len(numero) -1) / 2)

        ultimaPosicion = len(numero) -1 # Almacenamos la última posición. -1 al trabajar desde la posición 0 a la última -1

        for i in range(numerosHastaMitad):
            if(numero[i] != numero[ultimaPosicion-i]):
                return 0 # No se cumple la condición, descartamos que sea un palíndromo

    return 1 # Se han superado los filtros anteriores, es un palíndromo

def esPrimo(numero):
    
    contador = 2 # Variable que dividiremos por el número para comprobar si es primo
    
    while(contador < int(numero)): # El contador irá desde el número 2 hasta nuestro número -1

        if(int(numero) % contador == 0): return 0 # No es un número primo, es divisible por otro número
        contador = contador +1 # Incrementamos nuestro contador

    return 1

numPalindromos = 0 # Contador de números palíndromos
numPrimos = 0 # Contador de números primos
palindromosPrimos = [] # Lista de números que son palíndromos y primos a la vez

# Creamos una variable para el fichero de entrada y otra para el fichero de salida
ficheroEntrada=sys.argv[1]
ficheroSalida=sys.argv[2]

esPalindromo("121")

fichero = open(ficheroEntrada) # Abrimos el fichero que contiene los números
for numero in fichero:
    numero = numero.replace("\n", "") # Eliminamos los saltos de línea

    palindromo = esPalindromo(numero) # Llamamos a la función esPalindromo y guardamos su respuesta
    numPalindromos += palindromo # Aumentamos su valor si es palindromo. 1 = palindromo, 0 = no palindromo

    primo = esPrimo(numero) # Llamamos a la funcion esPrimo y guardamos su respuesta
    numPrimos += primo # Aumentamos su valor si es primo. 1 = primo, 0 = no primo

    if palindromo == 1 and primo == 1: # Si tenemos un número tanto primo como palíndromo lo guardaremos en nuestra lista
        palindromosPrimos.append(numero)

# Volvamos los datos en el fichero de salida indicado por el usuario
with open(ficheroSalida, 'w') as f:
    f.write("Hay " + str(numPalindromos) + " numeros palindromos\n") # Escribimos los números palíndromos
    f.write("Hay " + str(numPrimos) + " numeros primos\n") # Escribimos los números primos

    for num in palindromosPrimos: # Escribimos los números que son primos y palíndromos a la vez
        f.write(str(num) + '\n')
