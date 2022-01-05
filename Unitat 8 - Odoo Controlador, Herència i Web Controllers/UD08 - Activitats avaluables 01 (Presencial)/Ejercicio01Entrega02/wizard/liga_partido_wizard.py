# -*- coding: utf-8 -*-
from odoo import models, fields

#Esta clase observamos que hereda de "models.TransientModel" una clase especial
#que crea un modelo, pero es temporal y no hacer permanente sus datos en la base de datos.
#Se utiliza para "mientras dura el Wizard"
class LigaPartidoWizard(models.TransientModel):
    _name = 'liga.partido.wizard'
    #Campos del modelo que usaremos en el Wizard
    
    #Nombre del equipo que juega en casa casa
    equipo_casa = fields.Many2one(
        'liga.equipo',
        string='Equipo local',
    )
    #Goles equipo de casa
    goles_casa= fields.Integer()

    #Nombre del equipo que juega fuera
    equipo_fuera = fields.Many2one(
        'liga.equipo',
        string='Equipo visitante',
    )
    #Goles equipo de casa
    goles_fuera= fields.Integer()

    #Funcion que se llamara desde el Wizard, para utilizando este modelo temporal
    #y con el crear un nuevo registro en el modelo destino
    def add_liga_partido(self):
        #Obtenemos referencia al modelo destino
        ligaPartidoModel = self.env['liga.partido']
        #Tenemos que recorrer porque recordamos self referencia a todo el modelo
        for wiz in self:
            #Por cada elemento (en verdad, este Wizars solo tendra uno)
            #Creamos un registro en "liga.partido"
            ligaPartidoModel.create({
                'equipo_casa': wiz.equipo_casa.id,
                'goles_casa': wiz.goles_casa,
                'equipo_fuera': wiz.equipo_fuera.id,
                'goles_fuera': wiz.goles_fuera,
            })
