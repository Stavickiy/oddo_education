from odoo import models, fields

class Clinic(models.Model):
    _name = 'clinic'
    _description = 'Clinic'

    name = fields.Char(string='Clinic Name', required=True)
    doctor_ids = fields.Many2many('doctor', 'clinic_id', string='Doctors')
    patient_ids = fields.One2many('patient', 'clinic_id', string='Patients')
