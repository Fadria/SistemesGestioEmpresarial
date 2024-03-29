# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de datos
class Paciente(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'paciente'

    _description = 'Modelo de la lista de pacientes del hospital'

    #Como no tenemos un atributo "name" en nuestro modelo, indicamos que cuando
    #se necesite un nombre, se usara el atributo nombre_completo
    _rec_name="nombre_completo"

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    # Campos del paciente
    nombre_completo = fields.Char()
    # Texto avanzado, nos permite uso de negrita, párrafos, etc
    sintomas = fields.Html('Síntomas del paciente', sanitize=True, strip_style=False) 