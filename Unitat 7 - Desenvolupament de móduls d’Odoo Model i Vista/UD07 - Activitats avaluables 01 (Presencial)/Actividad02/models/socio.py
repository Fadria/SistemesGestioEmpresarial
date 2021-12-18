# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de datos
class Socio(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'socio'

    _description = 'Modelo de la lista de socios de la biblioteca'

    #Como no tenemos un atributo "name" en nuestro modelo, indicamos que cuando
    #se necesite un nombre, se usara el atributo tarea
    _rec_name="identificador"

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    identificador = fields.Char()
    nombre = fields.Char()
    apellidos = fields.Char()
