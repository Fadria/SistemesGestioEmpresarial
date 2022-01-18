# -*- coding: utf-8 -*-
from odoo import models, fields

#Esta clase observamos que hereda de "models.TransientModel" una clase especial
#que crea un modelo, pero es temporal y no hacer permanente sus datos en la base de datos.
#Se utiliza para "mientras dura el Wizard"
class RepartosWizard(models.TransientModel):
    _name = 'repartos.wizard'

    # Variable de donde obtendremos los estados del reparto
    ESTADOSREPARTO = [
        ('nohasalido', 'No ha salido'),
        ('encamino', 'En camino'),
        ('entregada', 'Entregada')
    ]

    # Campo con un valor que será auto incremental y asignado directamente
    reparto_id = fields.Integer(string = "ID Reparto", readonly = True, default = lambda self: self.env['ir.sequence'].next_by_code('increment_your_field'))
    fecha_comienzo = fields.Datetime("Fecha y hora de comienzo")
    repartidor = fields.Many2one("empleados", "Repartidor") # Relación con el modelo empleados
    vehiculo = fields.Many2one("vehiculos", "Vehículo") # Relación con el modelo vehículo
    estado = fields.Selection(ESTADOSREPARTO, default=ESTADOSREPARTO[0][0]) # Campo de selección con las opciones de la variable ESTADOSREPARTO
    emisor = fields.Many2one("clientes", "Emisor") # Relación con el modelo clientes
    receptor = fields.Many2one("clientes", "Receptor") # Relación con el modelo clientes

    #Funcion que se llamara desde el Wizard, para utilizando este modelo temporal
    #y con el crear un nuevo registro en el modelo destino
    def add_reparto(self):
        #Obtenemos referencia al modelo destino
        RepartosModel = self.env['repartos']
        #Tenemos que recorrer porque recordamos self referencia a todo el modelo
        for wiz in self:
            #Por cada elemento (en verdad, este Wizars solo tendra uno)
            #Creamos un registro en "repartos"
            RepartosModel.create({
                'reparto_id': wiz.reparto_id,
                'fecha_comienzo': wiz.fecha_comienzo,
                'repartidor': wiz.repartidor.id,
                'vehiculo': wiz.vehiculo.id,
                'estado': wiz.estado,
                'emisor': wiz.emisor.id,
                'receptor': wiz.receptor.id,
            })
