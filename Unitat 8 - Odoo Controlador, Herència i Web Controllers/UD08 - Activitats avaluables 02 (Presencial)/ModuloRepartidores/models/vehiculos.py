# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Vehiculos(models.Model):
    # Nombre y descripcion del modelo
    _name = 'vehiculos'
    _description = 'Vehiculos de la empresa de transporte'

    # ATRIBUTOS

    # PARA CUANDO NO HAY UN ATRIBUTO LLAMADO NAME PARA MOSTRAR NOMBRE DE UN REGISTRO
    # https://www.odoo.com/es_ES/forum/ayuda-1/how-defined-display-name-in-custom-many2one-91657
    
    # Indicamos que atributo sera el que se usara para mostrar nombre.
    # Por defecto es "name", pero si no hay un atributo que se llama name, aqui lo indicamos
    # Aqui indicamos que se use el atributo "matricula"
    _rec_name = 'matricula'    


    # Variable de donde obtendremos los tipos de vehículos usados en la empresa
    TIPOSVEHICULO = [
        ('ciclomotor', 'Ciclomotor'),
        ('furgoneta', 'Furgoneta')
    ]

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields

    tipo = fields.Selection(TIPOSVEHICULO, default=TIPOSVEHICULO[0][0]) # Campo de selección con las opciones de la variable TIPOSVEHICULO
    matricula = fields.Char("Matrícula")
    foto = fields.Image('Foto Vehículo',max_width=50,max_height=50)
    #Campo con HTML (Sanitizado) donde se guarda la descripción del vehículo
    descripcion = fields.Html('Descripción', sanitize=True, strip_style=False)