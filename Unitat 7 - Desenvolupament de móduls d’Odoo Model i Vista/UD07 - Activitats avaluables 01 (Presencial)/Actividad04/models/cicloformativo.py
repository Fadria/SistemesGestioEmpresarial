# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de datos
class Cicloformativo(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'cicloformativo'

    _description = 'Modelo de la lista de ciclos del instituto'

    #Como no tenemos un atributo "name" en nuestro modelo, indicamos que cuando
    #se necesite un nombre, se usara el atributo nombre_completo
    _rec_name="ciclo"

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    # Campos del ciclo
    ciclo = fields.Char()
    modulos = fields.Many2many('modulo')
