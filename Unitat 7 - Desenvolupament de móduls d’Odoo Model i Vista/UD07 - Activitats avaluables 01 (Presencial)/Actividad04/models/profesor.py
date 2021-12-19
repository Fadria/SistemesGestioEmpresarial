# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de datos
class Profesor(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'profesor'

    _description = 'Modelo de la lista de profesores del instituto'

    #Como no tenemos un atributo "name" en nuestro modelo, indicamos que cuando
    #se necesite un nombre, se usara el atributo nombre_completo
    _rec_name="nombre_completo"

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    # Campos del profesor
    nombre_completo = fields.Char()
    dni = fields.Char()
    email = fields.Char()
    telefono = fields.Integer()
    fecha_nacimiento = fields.Date()
    ciudad = fields.Char()
    provincia = fields.Char()
    direccion = fields.Char()