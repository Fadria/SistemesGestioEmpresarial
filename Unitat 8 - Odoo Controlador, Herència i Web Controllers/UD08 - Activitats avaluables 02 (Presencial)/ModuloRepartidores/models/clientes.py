# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Clientes(models.Model):
    # Nombre y descripcion del modelo
    _name = 'clientes'
    _description = 'Clientes de la empresa de transporte'

    # Parametros de ordenacion por defecto
    _order = 'apellidos'

    # ATRIBUTOS

    # PARA CUANDO NO HAY UN ATRIBUTO LLAMADO NAME PARA MOSTRAR NOMBRE DE UN REGISTRO
    # https://www.odoo.com/es_ES/forum/ayuda-1/how-defined-display-name-in-custom-many2one-91657
    
    # Indicamos que atributo sera el que se usara para mostrar nombre.
    # Por defecto es "name", pero si no hay un atributo que se llama name, aqui lo indicamos
    # Aqui indicamos que se use el atributo "dni"
    _rec_name = 'dni'    

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields

    dni = fields.Char("DNI")
    nombre = fields.Char("Nombre")
    apellidos = fields.Char("Apellidos")
    telefono = fields.Char("Teléfono")