# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api
from datetime import date


class Patient(models.Model):
    _name = 'hospital_management.patient'
    _inherit = 'hospital_management.person'
    _description = 'Patient'

    birth_date = fields.Date(string='Birth Date', required=True)
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    passport_data = fields.Char(string='Passport Data')
    contact_person_id = fields.Many2one('hospital_management.contact.person', string='Contact Person', options="{'no_create': False}")
    personal_doctor_id = fields.Many2one('hospital_management.doctor', string='Personal Doctor')

    @api.depends('birth_date')
    def _compute_age(self):
        for patient in self:
            if patient.birth_date:
                today = date.today()
                patient.age = today.year - patient.birth_date.year - (
                            (today.month, today.day) < (patient.birth_date.month, patient.birth_date.day))
            else:
                patient.age = 0
