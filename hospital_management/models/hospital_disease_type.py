from odoo import models, fields


class DiseaseType(models.Model):
    _name = 'hospital_management.disease.type'
    _description = 'Disease Type'
    _parent_store = True
    _parent_name = 'parent_id'
    _rec_name = 'name'

    name = fields.Char(string='Type Name', required=True)
    parent_id = fields.Many2one('hospital_management.disease.type', string='Parent Type', ondelete='restrict', domain="[('id', '!=', id)]")
    child_ids = fields.One2many('hospital_management.disease.type', 'parent_id', string='Subtypes')
    parent_path = fields.Char(index=True)
