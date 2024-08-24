# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = "Estate Property Offer"

    price = fields.Float()
    status = fields.Selection(copy=False, selection=[
        ('Accepted', 'Accepted'),
        ('refused', 'Refused')
    ])
    partner_id = fields.Many2one('res.partner', string='Partners', equired=True)
    property_id = fields.Many2one('estate_property', equired=True)
