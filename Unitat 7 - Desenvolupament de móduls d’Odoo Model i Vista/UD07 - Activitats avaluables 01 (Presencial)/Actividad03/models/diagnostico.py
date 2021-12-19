# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de datos
class Diagnostico(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'diagnostico'

    _description = 'Modelo de la lista de diagnósticos del hospital'

    #Como no tenemos un atributo "name" en nuestro modelo, indicamos que cuando
    #se necesite un nombre, se usara el atributo paciente
    _rec_name="paciente"

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    # Campos del diagnóstico
    paciente = fields.Many2one('paciente')
    medico = fields.Many2one('medico')
    # Texto avanzado, nos permite uso de negrita, párrafos, etc
    sintomas = fields.Html('Síntomas del paciente', sanitize=True, strip_style=False) 