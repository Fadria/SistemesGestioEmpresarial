# -*- coding: utf-8 -*-
from typing import Sequence
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Repartos(models.Model):
    # Nombre y descripcion del modelo
    _name = 'repartos'
    _description = 'Repartos de la empresa de transporte'

    # Parametros de ordenacion por defecto
    _order = 'fecha_comienzo'

    # ATRIBUTOS

    # PARA CUANDO NO HAY UN ATRIBUTO LLAMADO NAME PARA MOSTRAR NOMBRE DE UN REGISTRO
    # https://www.odoo.com/es_ES/forum/ayuda-1/how-defined-display-name-in-custom-many2one-91657
    
    # Indicamos que atributo sera el que se usara para mostrar nombre.
    # Por defecto es "name", pero si no hay un atributo que se llama name, aqui lo indicamos
    # Aqui indicamos que se use el atributo "nombre"
    _rec_name = 'reparto_id'    

    # Variable de donde obtendremos los estados del reparto
    ESTADOSREPARTO = [
        ('nohasalido', 'No ha salido'),
        ('encamino', 'En camino'),
        ('entregada', 'Entregada')
    ]

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
    reparto_id = fields.Integer(string = "ID Reparto", readonly = True, default = lambda self: self.env['ir.sequence'].next_by_code('increment_your_field'))
    fecha_comienzo = fields.Datetime("Fecha y hora de comienzo")
    fecha_regreso = fields.Datetime("Fecha y hora de regreso")
    fecha_recepcion = fields.Datetime("Fecha y hora de recepcióon")
    repartidor = fields.Many2one("empleados", "Repartidor")
    vehiculo = fields.Many2one("vehiculos", "Vehículo")
    kilometros = fields.Float("Kilómetros")
    peso = fields.Float("Peso en KG")
    volumen = fields.Float("Volumen del paquete")
    #Campo con HTML (Sanitizado) donde se guarda la descripción del vehículo
    observaciones = fields.Html('Descripción', sanitize=True, strip_style=False)
    estado = fields.Selection(ESTADOSREPARTO, default=ESTADOSREPARTO[0][0])
    emisor = fields.Many2one("clientes", "Emisor")
    receptor = fields.Many2one("clientes", "Receptor")