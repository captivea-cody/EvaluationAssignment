# -*- coding: utf-8 -*-

{
    'name': 'EPL Data Module',
    'version': '69',
    'summary': 'A bunch of silly soccer faff.',
    'description': """Soccer is cool
                """,
    'category': 'Evaluation Assignment',
    'author': 'Cody Wiggins',
    'depends': 
    ['base',
     'mail',
    ],
    'website': 'https://www.captivea.com/',
    'data': [
        'views/epl_view.xml',
        'data/club_nat_player_data.xml',
    ],
    'images': ['static/description/icon.png'],
    'license': 'OPL-1',
    'installable': True,
    'auto_install': False,
    'application': True,
    "cloc_exclude": ["./**/*"],  # exclude all files in a module recursively
}
