# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Empleados(models.Model):
    # Nombre y descripcion del modelo
    _name = 'empleados'
    _description = 'Empleados de la empresa de transporte'

    # Parametros de ordenacion por defecto
    _order = 'nombre'

    # ATRIBUTOS

    # PARA CUANDO NO HAY UN ATRIBUTO LLAMADO NAME PARA MOSTRAR NOMBRE DE UN REGISTRO
    # https://www.odoo.com/es_ES/forum/ayuda-1/how-defined-display-name-in-custom-many2one-91657
    
    # Indicamos que atributo sera el que se usara para mostrar nombre.
    # Por defecto es "name", pero si no hay un atributo que se llama name, aqui lo indicamos
    # Aqui indicamos que se use el atributo "nombre"
    _rec_name = 'nombre'    

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields

    nombre = fields.Char("Nombre")
    apellidos = fields.Char("Apellidos")
    dni = fields.Char("DNI")
    telefono = fields.Char("Teléfono")
    carnet_ciclomotor = fields.Boolean("Carnet de ciclomotor")
    carnet_furgoneta = fields.Boolean("Carnet de furgoneta")
    foto = fields.Image('Foto Empleado', max_width=50, max_height=50)
    repartos = fields.One2many("repartos", "repartidor")
