import pandas as pd # Liberaría para leer ficheros csv
import sys # Liberaría usada para leer parámetros desde consola

import barcode # Librería del código de barras
from barcode import EAN13 # Librería para generar un código de barras en formato EAN13
from barcode.writer import ImageWriter # Librería usada para generar la imagen del código de barras

nombreFichero = sys.argv[1] # Variable que contiene el nombre del fichero csv a leer

df2 = pd.read_csv(nombreFichero, header=None) # Leemos el fichero
listadoNombres = df2[0] # La primera columna contiene los nombres
listadoCodigos = df2[1] # La segunda columna contiene los números

# Bucle for que se encarga de recorrer la lista de nombres, asumimos que tendremos el mismo número de nombres y códigos en el CSV
for i in range(len(listadoNombres)):
    EAN = barcode.get_barcode_class('ean13') # Obtenemos la clase correspondiente al EAN13
    ean = EAN(str(listadoCodigos[i]), writer=ImageWriter()) # Variable para el código EAN de cada alumno
    nombreFichero = ean.save(str(listadoNombres[i])) # Generamos la imagen de cada código