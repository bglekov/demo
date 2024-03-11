{
    'name': 'HR Hospital',
    'summary': 'HR moodule lesson 2',

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
        'data/hh_master.xml',
        'views/hh__main__menu.xml',
        'views/hh_doctor_views.xml',
        'views/hh_illness_views.xml',
        'views/hh_patient_views.xml',
        'views/hh_patient_visit_views.xml',
        'views/hh_diagnosis.xml',
        'views/hh_contact_persons.xml',

    ],
    'demo': [
        'data/hh_demo.xml'



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
