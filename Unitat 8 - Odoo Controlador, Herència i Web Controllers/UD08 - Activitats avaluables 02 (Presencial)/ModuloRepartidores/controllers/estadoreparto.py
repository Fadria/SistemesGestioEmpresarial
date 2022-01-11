# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

# Clase del controlador web

class EstadoReparto(http.Controller):
    
    '''
    LLamada web para obtener el estado de un reparto.
    
    
    Decorador que indica que la url "/reparto/<codigo>" atendera por HTTP, sin autentificacion
    Devolvera texto plano que contendrá el estado del reparto
    Se puede probar accediendo a http://localhost:8069/reparto/2
    '''

    @http.route('/reparto/<codigo>', auth='public', cors='*', type='http')
    def obtenerEstadoRepartos(self, codigo, **kw):
        # Obtenemos una lista de repartos cuya id de reparto coincida con la proporcionada en la url
        repartos = request.env['repartos'].sudo().search([('reparto_id', '=', codigo)])

        # Como las ids no se repetirán, obtendremos el primer reparto y mostraremos su estado
        return str(repartos[0].estado)