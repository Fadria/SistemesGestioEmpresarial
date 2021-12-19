# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

from datetime import timedelta

#Definimos el modelo de datos
class PrestamoLibros(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'prestamo.libros'

    _description = 'Modelo de la lista de préstamos de libros de la biblioteca'

    #Como no tenemos un atributo "name" en nuestro modelo, indicamos que cuando
    #se necesite un nombre, se usara el atributo comicPrestamo
    _rec_name="comicPrestamo"

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields

    # Campos usados para indicar la duración del préstamo
    fecha_comienzo = fields.Date()
    fecha_finalizacion = fields.Date()

    # Relaciones con comic y con socio
    comicPrestamo = fields.Many2one('biblioteca.comic')
    socioPrestamo = fields.Many2one('socio')

    # Función que nos va a servir para comprobar si la fecha en la que comienza el préstamo es hoy o anterior
    @api.constrains('fecha_comienzo')
    def _check_fecha_comienzo(self):
        for record in self:            
            if (fields.Date.today() < record.fecha_comienzo):
                raise models.ValidationError('La fecha del comienzo del préstamo no puede ser posterior al día de hoy')

    # Función que nos va a servir para comprobar si la fecha en la que finaliza el préstamo es mañana o posterior
    @api.constrains('fecha_finalizacion')
    def _check_fecha_finalizacion(self):
        for record in self:
            if (fields.Date.today() > record.fecha_finalizacion):
                raise models.ValidationError('La fecha de finalización del préstamo debe ser mañana como mínimo')