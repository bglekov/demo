{
    'name': 'My demo module',
    'summary': 'My demo module from video',

    'author': 'BoricH',
    'website': '',

    'category': 'Castomization',
    'license': 'OPL-1',
    'version': '17.0.0.0.1',

    'depends': [
        'base',
    ],
    'external_dependencies': {'python': [], },

    'data': [
        'sequrity/ir.model.access.csv',
        'views/my_demo_views.xml',

    ],
    'demo': [
        'demo/my_demo.xml'

    ],

    'installable': True,
    'auto_install': False,
    'application': False,

    'images': [
        'static/description/icon.png',
    ],

    'price': 0,
    'currency': 'EUR',
}
