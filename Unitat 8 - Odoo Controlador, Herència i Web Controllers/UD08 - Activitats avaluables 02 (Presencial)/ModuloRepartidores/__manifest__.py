# -*- coding: utf-8 -*-
{
    'name': "ModuloRepartidores",  # Titulo del módulo
    'summary': "Módulo destinado a ser utilizado por empresas de transportes para controlar los diferentes datos de ella",  # Resumen de la funcionaliadad
    'description': """
    Módulo empresa de transportes
    ==============
    """,  

    #Indicamos que es una aplicación
    'application': True,
    'author': "Federico Adria",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],

    'data': [      
        'security/ir.model.access.csv',

        #Aqui distintas vistas de equipo (vistas diferentes, mismo modelo)
        'views/empleados.xml',
        'views/vehiculos.xml',
        'views/clientes.xml',
        'views/repartos.xml',

        'report/entregas_report.xml',

        'wizard/repartos_wizard.xml'
    ],
    # Fichero con data de demo si se inicializa la base de datos con "demo data" (No incluido en ejemplo)
    # 'demo': [
    #     'demo.xml'
    # ],
}
