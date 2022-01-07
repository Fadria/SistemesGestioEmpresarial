# -*- coding: utf-8 -*-
{
    'name': "Ejercicio04Entrega02",  # Titulo del módulo
    'summary': "A partir de una llamada web, genera un codigo de barras y imágenes aleatorias",  # Resumen de la funcionaliadad
    'description': """
    A partir de una llamada web, genera un codigo de barras y en otra una imagen aleatoria
    ==============
    """,  

    #Indicamos que es una aplicación
    'application': True,
    'author': "Federico Adria",
    'website': "http://apuntesfpinformatica.es",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],

    #IMPORTANTE: Si estais usando Docker Compose, debeis instalar la dependencia:
    #docker-compose exec web bash
    #y tras ello pip3 instal python-barcode y luego pip3 install python-barcode[images]

    # Para la librería Pillow usaríamos python3 -m pip install --upgrade pip

    #Dependencias externas de https://pypi.org/project/python-barcode/
    'external_dependencies': {"python": ['python-barcode',"python-barcode[images]", "PIL"], "bin": []},
    'data': [
    ],
    # Fichero con data de demo si se inicializa la base de datos con "demo data" (No incluido en ejemplo)
    # 'demo': [
    #     'demo.xml'
    # ],
}
