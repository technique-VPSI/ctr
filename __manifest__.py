# -*- coding: utf-8 -*-
{
    'name': "ctr",

    'summary': """
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "lamrabti abdellatif",
    'website': "http://www.vpsi.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['helpdesk'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
}
