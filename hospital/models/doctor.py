from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Doctor(models.Model):
    _inherit = 'res.users'

    user_id = fields.Many2one('res.users', string='Salesman', default=lambda self: self.env.user)
    clinic_ids = fields.Many2many('clinic', string='Clinics')
    photo = fields.Image(related="res.users.photo", store=True)

    _sql_constraints = [
        ('unique_user', 'unique(user_id)', 'Each user can only be assigned to one doctor!')
    ]

    @api.constrains('user_id')
    def _check_unique_user(self):
        if self.search_count([('user_id', '=', self.user_id.id)]) > 1:
            raise ValidationError('Each user can only be assigned to one doctor!')