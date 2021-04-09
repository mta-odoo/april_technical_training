# -*- coding: utf-8 -*-
{
    'name': "Galeria de Arte!!",

    'summary': """
        Mostrar Obras de Arte""",

    'description': """
        Mostrar Obras de Arte
    """,

    'author': "Odoo",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Training',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/art_security.xml',
        'security/ir.model.access.csv',
        'views/gallery_menuitems.xml',
        'views/gallery_views.xml',
        'data/art_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}