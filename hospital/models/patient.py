# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _


class Patient(models.Model):
    _name = "appointment.patient"
    _description = "Patient model"
    _order = "surname,first_name"

    first_name = fields.Char(required=True)
    surname = fields.Char(required=True)
    date_of_birth = fields.Date()
    doctor = fields.Many2one('appointment.doctor')
    phone_number = fields.Char(required=True)
    anamnesis = fields.Text()
    photo = fields.Image()
    city = fields.Char()
    clinic = fields.Many2one('appointment.clinic', required=True)
    instagram = fields.Char()
    telegram = fields.Char()


