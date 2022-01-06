# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

#Necesario para trabajar con base64
import base64
#Biblioteca para guardar la imagen en memoria antes de pasarla a base64
from io import BytesIO
#Bibiliotecas (hay que instalarlas, son dependencias, ver "__manifest__.py")
import barcode
from barcode.writer import ImageWriter

from PIL import Image
import os
import io

# Clase del controlador web
class GenerarBarcode(http.Controller):
    
    '''
    LLamada web para generar una imagen con un codigo de barras.
    
    
    Decorador que indica que la url "/generador/numero" atendera por HTTP, sin autentificacion
    Se puede probar accediendo a http://localhost:8069/generador/1
    Y nos devolvera via web una imagen con el codigo de barras generado

    '''

    @http.route('/generador/<codigo>', auth='public', cors='*', type='http')
    def crearBarcode(self, codigo, **kw):
        #Formato del codigo de barras ean13
        EAN = barcode.get_barcode_class('ean13')
        #Generamos el codigo de barras de 12 digitos. El zfill es para rellenar 0s hasta 12
        ean = EAN(str(codigo).zfill(12), writer=ImageWriter())
        #Declaramos un flujo de bytes (guardaremos ahi la imagen)
        fp = BytesIO()
        #Guardamos la imagen en el flujo de bytes
        ean.write(fp)
        #PAsamos el flujo de bytes y lo codificamos en base 64
        img_str = base64.b64encode(fp.getvalue()).decode("utf-8")
        #Devolvemos el HTML que muestra la imagen generada, pasada como base64
        return '<div><img src="data:image/png;base64,'+str(img_str)+'"/></div>'

    # URL Ejemplo: http://localhost:8069/generarImagen/500/500
    @http.route('/generarImagen/<ancho>/<largo>', auth='public', cors='*', type='http')
    def crearImagen(self, ancho, largo, **kw): # Recibimos el ancho y largo de la URL
        size = (int(ancho), int(largo)) # Tamaño de la imagen
        im = Image.new('RGB', size) # Creamos la imagen

        def ran():
            return os.urandom(int(ancho)*int(largo))

        pixels = zip(ran(), ran(), ran()) # Obtenemos una lista con los píxeles de la foto
        im.putdata(list(pixels)) # Añadimos los datos a nuestra imagen
        
        # Obtenemos el valor de la imagen
        with io.BytesIO() as output:
            im.save(output, format="JPEG")
            contents = output.getvalue()
        
        # Mostramos la imagen en la URL solicitada por el usuario
        return '<div><img src="data:image/jpeg;base64,'+str(base64.b64encode(contents).decode("utf-8"))+'"/></div>'