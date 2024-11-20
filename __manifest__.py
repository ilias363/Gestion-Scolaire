# -*- coding: utf-8 -*-
{
    'name': 'Gestion scolaire',
    'author': 'Ilias OUADDAF & Aymane FAJR EL IDRISS',
    'version': '1.0',
    'summary': 'Gestion des étudiants et des classes',
    'sequence': 15,
    'description': """
    Gestion des étudiants et des classes
    ======================================
    Ce module permet de gérer les étudiants et les classes dans un établissement scolaire.
    """,
    'category': 'Education/Management',
    'website': 'https://www.example.com',
    'images': ['static/description/icon.png'],
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/main_menu.xml',
        'views/etudiant_views.xml',
        'views/classe_views.xml',
        'views/filiere_views.xml',
        'views/formateur_views.xml',
        'views/classe_report.xml',
        'views/ir_cron_view.xml',
        'wizard/wizard_test_view.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
