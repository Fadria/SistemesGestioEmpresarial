from pyzbar.pyzbar import decode # Librería para leer códigos de barras y QR
import cv2 # Librería usada para leer imágenes
import os # Importamos la librería necesaria para trabajar con los ficheros y directorios del sistema operativo

listaFicheros = os.listdir(".") # Obtenemos todos los ficheros y directorios de la ruta actual

for fichero in listaFicheros: # Bucle donde trabajaremos con cada fichero
    nombreAlumno = fichero.split(".")[0] # Obtenemos el nombre del alumno, que es el nombre del fichero sin la extensión
    extension = fichero.split(".")[1] # Obtenemos la extensión, que deberá ser PNG para proceder, es decir, una imagen

    if extension == "png": # Si se trata de un PNG continuamos

        img = cv2.imread(fichero) # Leemos la imagen y obtenemos una varible de tipo lista
        
        # Decodificamos el código de barras, el cual es un array, podríamos detectar varios códigos en la misma imagen incluso
        detectedBarcodes = decode(img)

        # Si no se ha detectado un código de barras informaremos de ello
        if not detectedBarcodes:
            print("Error, no se ha detectado un código de barras en el fichero: " + str(fichero))
        else:
            # Traverse through all the detected barcodes in image
            for barcode in detectedBarcodes:                     
                # Imprimimos el nombre del alumno(fichero) y su ID
                    print("Alumno: " + nombreAlumno + " con ID: " + str(barcode.data))