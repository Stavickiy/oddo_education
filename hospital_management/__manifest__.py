# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Hospital manegment',
    'description': 'Hospital manegment system',
    'category': 'Services',
    'depends': ['base'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/hospital_management_patient_view.xml',
        'views/hospital_management_doctor_view.xml',
        'views/hospital_management_disease_directory_view.xml',
        'views/hospital_management_disease_type_view.xml',
        'views/hospital_management_contact_person_view.xml',
        'views/disease_type_views.xml',
        'views/hospital_management_menus.xml',
    ]
}
