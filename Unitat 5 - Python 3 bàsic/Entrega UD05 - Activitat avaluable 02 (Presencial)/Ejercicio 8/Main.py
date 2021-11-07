import os # Importamos la librería necesaria para trabajar con los ficheros y directorios del sistema operativo
import shutil # Importamos la libería necesaria para mover ficheros

listaFicheros = os.listdir(".") # Obtenemos todos los ficheros y directorios de la ruta actual
listaExtensiones = ["txt", "png", "mp3", "doc"] # Lista de extensiones que queremos organizar

for fichero in listaFicheros: # Bucle donde trabajaremos con cada fichero
    extensionFichero = os.path.splitext(fichero)[1].replace(".","") # Obtenemos la extensión del fichero sin punto
    
    # Si el fichero tiene una extensión de nuestro listado procedemos
    if extensionFichero in listaExtensiones:
        # Creamos el directorio con el nombre de la extensión del fichero siempre que no exista
        if not os.path.exists(extensionFichero) and extensionFichero != "":
            os.makedirs(extensionFichero) # Creamos el directorio

        shutil.move (fichero, extensionFichero) # Movemos el fichero al directorio