# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

#Clase del controlador web
class Main(http.Controller):
    #Decorador que indica que la url "/ligafutbol/equipo/json" atendera por HTTP, sin autentificacion
    #Devolvera texto que estará en formato JSON
    #Se puede probar accediendo a http://localhost:8069/ligafutbol/equipo/json
    @http.route('/ligafutbol/equipo/json', type='http', auth='none')
    def obtenerDatosEquiposJSON(self):
        #Obtenemos la referencia al modelo de Equipo
        equipos = request.env['liga.equipo'].sudo().search([])
        
        #Generamos una lista con informacion que queremos sacar en JSON
        listaDatosEquipos=[]
        for equipo in equipos:
             listaDatosEquipos.append([equipo.nombre,str(equipo.fecha_fundacion),equipo.jugados,equipo.puntos,equipo.victorias,equipo.empates,equipo.derrotas])
        #Convertimos la lista generada a JSON
        json_result=json.dumps(listaDatosEquipos)

        return json_result

    # Indicamos la URL donde ejecutaremos la siguiente función
    # Lo ejecutaríamos en la URL http://localhost:8069/ligafutbol/eliminarempates
    @http.route('/ligafutbol/eliminarempates', auth='public', website=True)
    def eliminarEmpatesPartidos(self, **kw):
        # Variable que usaremos para contar cada empate que eliminamos
        partidosEliminados = 0

        # En primer lugar obtenemos el listado de todos los partidos
        listadoPartidos = request.env['liga.partido'].sudo().search([])

        for partido in listadoPartidos: # Acciones ejecutadas para cada partido
            if (partido.goles_casa == partido.goles_fuera): # Si los dos equipos marcan los mismos goles procederemos
                partidosEliminados += 1 # Aumentamos en 1 la cantidad de partidos eliminados
                partido.unlink() # Eliminamos el registro de la base de datos

        request.env['liga.partido'].actualizoRegistrosEquipo() # Actualizamos la clasificación

        # Mostramos un mensaje al usuario informando el total de partidos eliminados
        return "Se han eliminado un total de " + str(partidosEliminados) + " partidos que eran empates."