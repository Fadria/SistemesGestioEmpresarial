import pyperclip # Librería usada para trabajar con el portapapeles
import sys # Liberaría usada para leer parámetros desde consola

print("Esperando a que copie un texto...") # Avisamos al usuario de que el programa está esperando a que copie en el portapapeles
pyperclip.waitForNewPaste() # Esperamos hasta que el usuario copie algo

# Para comprobar el funcionamiento de la aplicación, recomendamos copiar esta cadena: Hola a todos, viva PyThON

'''
     En nuestra variable almacenaremos la cadena copiada por el usuario y la pasaremos a minúsculas. Esto es debido a que queremos
     que el programa no sea casesensitive, es decir, que se censure sin importar si algo es escrito en mayúsculas, minúsculas o una
     combinación de ellas. Por ello, cada palabra a censurar  también la pasaremos a minúsculas en posteriores líneas.
'''
cadenaCopiada = pyperclip.paste().lower()

fichero = open(sys.argv[1]) # Abrimos el fichero que nos indica el usuario

for palabraProhibida in fichero: # Cada línea del fichero corresponderá a una palabra prohibida
    palabraProhibida = palabraProhibida.replace("\n", "").lower() # Eliminamos el salto de línea de la cadena y pasamos a minúsculas
    if palabraProhibida in cadenaCopiada: # Si la palabra prohibida se encuentra en el texto que hemos copiado realizaremos las siguientes acciones
        '''
            Para activar nuestro filtro, reemplazaremos todas las apariciones de palabras prohibidas en el texto copiado y las
            reemplazaremos por una serie de carácteres * cuya longitud será la misma que la de la palabra prohibida
        '''
        cadenaCopiada = cadenaCopiada.replace(palabraProhibida, "*" * len(palabraProhibida))

pyperclip.copy(cadenaCopiada) # Introducimos el valor de la cadena copiada ya censurada en el portapapeles
print("Ahora dispone de la cadena " + str(cadenaCopiada) + " en su portapapeles.")