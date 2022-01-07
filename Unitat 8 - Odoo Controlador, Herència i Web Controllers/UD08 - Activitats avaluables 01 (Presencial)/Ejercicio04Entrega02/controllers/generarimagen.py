# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

#Necesario para trabajar con base64
import base64

#Biblioteca para guardar la imagen en memoria antes de pasarla a base64
from io import BytesIO

from PIL import Image
import os
import io

# Clase del controlador web
class GenerarImagen(http.Controller):
    
    '''
        LLamada web para generar una imagen formada por píxeles aleatorios
        
        Decorador que indica que la url "/generadorImagen/<width>/<height>" atendera por HTTP, sin autentificacion
        Se puede probar accediendo a http://localhost:8069/generadorImagen/350/350
        Y nos devolvera via web una imagen con el codigo de barras generado
    '''

    @http.route('/generadorImagen/<width>/<height>', auth='public', cors='*', type='http')
    def generadorImagen(self, width, height, **kw): # Recibimos el ancho y largo de la URL

        # Funcion que usaremos para generar los bytes de la foto
        def generateBytes():
            return os.urandom(int(width) * int(height)) # Genera una cadena de bytes aleatorios

        area = (int(width), int(height)) # Area de la imagen
        imagen = Image.new('RGB', area) # Creamos la imagen

        pixelesFoto = zip(generateBytes(), generateBytes(), generateBytes()) # Obtenemos los pixeles de la foto
        imagen.putdata(list(pixelesFoto)) # Añadimos los datos a nuestra imagen
        
        # Obtenemos el contenido de la imagen
        with io.BytesIO() as output:
            imagen.save(output, format="JPEG") # Guardamos la imagen (sería dentro de nuestro contenedor)
            contents = output.getvalue() # variable que contendrá el valor de nuestra imagen
        
        # Mostramos la imagen en la URL solicitada por el usuario gracias a la variable que tiene su contenido
        imagenbase64 = str(base64.b64encode(contents).decode("utf-8"))
        return '<div><h1>Foto aleatoria:</h1><img src="data:image/jpeg;base64,'+ imagenbase64 + '"/></div>'