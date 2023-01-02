# -*- coding: utf-8 -*-

{
    'name': 'EPL Player Tracker',
    'version': '1.0',
    'summary': 'Tracks professional athletes competing in the English Premier League',
    'description': """ I like soccer too much
                """,
    'category': 'Product Lifecycle Management',
    'author': 'Cody Wiggins',
    'company': 'Captivea LLC',
    'maintainer': 'https://www.captivea.com/',
    'depends': 
    ['base',
     'mrp_plm',
     'mrp',
     'product',
     'stock',
     'account',
     'sale_product_configurator',
     'mail',
    ],
    'website': 'https://www.captivea.com/',
    'data': [
        'views/epl_view.xml',
        'data/club_nat_player_data.xml',
    ],
    'qweb': [],
    'images': ['static/description/icon.png'],
    'license': 'OPL-1',
    'installable': True,
    'auto_install': False,
    'application': True,
    "cloc_exclude": ["./**/*"],  # exclude all files in a module recursively
}
