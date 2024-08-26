from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate model"

    name = fields.Char(required=True, unique=True)

    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'The name must be unique!')
    ]
