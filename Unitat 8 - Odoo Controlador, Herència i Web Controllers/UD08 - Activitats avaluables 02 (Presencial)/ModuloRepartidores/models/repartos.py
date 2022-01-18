# -*- coding: utf-8 -*-
from typing import Sequence
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Repartos(models.Model):
    # Nombre y descripcion del modelo
    _name = 'repartos'
    _description = 'Repartos de la empresa de transporte'

    '''
        Parametros de ordenacion por defecto, en nuestro caso, pensamos que lo más adecuado es visualizar los pedidos más recientes
        y dentro de ellos, los de mayor urgencia
    '''
    _order = 'fecha_recepcion desc, urgencia_reparto desc'

    # ATRIBUTOS

    # PARA CUANDO NO HAY UN ATRIBUTO LLAMADO NAME PARA MOSTRAR NOMBRE DE UN REGISTRO
    # https://www.odoo.com/es_ES/forum/ayuda-1/how-defined-display-name-in-custom-many2one-91657
    
    # Indicamos que atributo sera el que se usara para mostrar nombre.
    # Por defecto es "name", pero si no hay un atributo que se llama name, aqui lo indicamos
    # Aqui indicamos que se use el atributo "reparto_id"
    _rec_name = 'reparto_id'    

    # Variable de donde obtendremos los estados del reparto
    ESTADOSREPARTO = [
        ('nohasalido', 'No ha salido'),
        ('encamino', 'En camino'),
        ('entregada', 'Entregada')
    ]

    '''
        Variable de donde obtendremos la urgencia del reparto, usamos números como valores para ordenar fácilmente los registros
        empleando este campo para ello
    '''
    URGENCIA = [
        ('4', 'Órganos Humanos'),
        ('3', 'Alimentos refrigerados'),
        ('2', 'Alimentos'),
        ('1', 'Alta prioridad'),
        ('0', 'Baja prioridad')
    ]

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields

    # Campo con un valor que será auto incremental y asignado directamente
    reparto_id = fields.Integer(string = "ID Reparto", readonly = True, default = lambda self: self.env['ir.sequence'].next_by_code('increment_your_field'))
    fecha_comienzo = fields.Datetime("Fecha y hora de comienzo")
    fecha_regreso = fields.Datetime("Fecha y hora de regreso")
    fecha_recepcion = fields.Datetime("Fecha y hora de recepción")
    repartidor = fields.Many2one("empleados", "Repartidor") # Relación con el modelo de empleados
    vehiculo = fields.Many2one("vehiculos", "Vehículo") # Relación con el modelo de vehículos
    kilometros = fields.Float("Kilómetros")
    peso = fields.Float("Peso en KG")
    volumen = fields.Float("Volumen del paquete")
    #Campo con HTML (Sanitizado) donde se guarda la descripción del vehículo
    observaciones = fields.Html('Descripción', sanitize=True, strip_style=False)
    estado = fields.Selection(ESTADOSREPARTO, default=ESTADOSREPARTO[0][0]) # Campo de selección con las opciones de la variable ESTADOSREPARTO
    urgencia_reparto = fields.Selection(URGENCIA, default=URGENCIA[4][0]) # Campo de selección con las opciones de la variable URGENCIA
    emisor = fields.Many2one("clientes", "Emisor") # Relación con el modelo de clientes
    receptor = fields.Many2one("clientes", "Receptor") # Relación con el modelo de clientes

    # Indicamos que esta funcion es una "Constraints" de ese atributo
    # Dicho de otra forma, cada vez que se cambie ese atributo, se lanzara esta funcion
    # Y si la funcion detecta un cambio inadecuado, cambiara una instruccion
    # Util cuando la constraint no se puede definir con sintaxis SQL y debe indicar en una funcion
    @api.constrains('vehiculo')
    def _check_validez_vehiculo(self):
        # Recorremos el modelo
        for record in self:
            # Comprobamos que los repartos de más de 10 kilómetros no se puedan hacer con ciclomotor
            if record.kilometros > 10 and record.vehiculo.tipo == "ciclomotor":
                # Levantamos un error para informar al usuario
                raise models.ValidationError('Los repartos de más de 10 kilómetros no se pueden realizar en ciclomotor.')

            # Comprobamos que los repartos de menos de 1 kilómetro no se puedan hacer con furgoneta
            elif record.kilometros < 1 and record.vehiculo.tipo == "furgoneta":
                # Levantamos un error para informar al usuario
                raise models.ValidationError('Los repartos de menos de 1 kilómetro no se pueden realizar en furgoneta.')

    # Indicamos que esta funcion es una "Constraints" de ese atributo
    # Dicho de otra forma, cada vez que se cambie ese atributo, se lanzara esta funcion
    # Y si la funcion detecta un cambio inadecuado, cambiara una instruccion
    # Util cuando la constraint no se puede definir con sintaxis SQL y debe indicar en una funcion
    @api.constrains('repartidor')
    def _validar_carnet_repartidor(self):
        # Recorremos el modelo
        for record in self:
            # Si es un reparto con ciclomotor y el repartidor no tiene el carnet lo informaremos en un error
            if record.vehiculo.tipo == "ciclomotor" and record.repartidor.carnet_ciclomotor == False:
                raise models.ValidationError('El repartidor indicado no tiene carnet de ciclomotor.')
            # Si es un reparto con furgoneta y el repartidor no tiene el carnet lo informaremos en un error
            elif record.vehiculo.tipo == "furgoneta" and record.repartidor.carnet_furgoneta == False:
                raise models.ValidationError('El repartidor indicado no tiene carnet de furgoneta.')

    # Indicamos que esta funcion es una "Constraints" de ese atributo
    # Dicho de otra forma, cada vez que se cambie ese atributo, se lanzara esta funcion
    # Y si la funcion detecta un cambio inadecuado, cambiara una instruccion
    # Util cuando la constraint no se puede definir con sintaxis SQL y debe indicar en una funcion
    @api.constrains('repartidor')
    def _validar_disponibilidad(self):
        # En primer lugar obtenemos el listado de todos los repartos
        repartos = self.env["repartos"].sudo().search([])

        for record in self: # Accederemos al reparto que estamos creando
            for reparto in repartos: # Acciones ejecutadas por cada reparto creado
                '''
                    Cuando obtenemos todos los repartos, ya tendríamos dentro de esta lista el reparto nuevo, por lo que siempre
                    levantaríamos el error cuando tenemos el estado "en curso", ya que lo comparamos consigo mismo.
                    Para evitar esto haremos que la id del reparto a comparar sea distinto a la del reparto a crear.
                '''
                if record.id != reparto.id:
                    # Si tenemos el mismo repartidor que en otro reparto en curso lanzaremos un error
                    if record.repartidor.dni ==  reparto.repartidor.dni and reparto.estado == "encamino" and record.estado == "encamino":
                        raise models.ValidationError('El repartidor ya se encuentra en un reparto')
                    # Si tenemos el mismo vehículo que en otro reparto en curso lanzaremos un error
                    elif record.vehiculo.matricula == reparto.vehiculo.matricula and reparto.estado == "encamino" and record.estado == "encamino":
                        raise models.ValidationError('El vehículo ya está en uso')