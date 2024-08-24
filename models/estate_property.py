# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate_property"
    _description = "Estate model"

    name = fields.Char(required=True)
    property_type_id = fields.Many2one("estate.property.type")
    tag_ids = fields.Many2many('estate.property.tag', string='Tags')
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string='Offers')
    salesman_id = fields.Many2one('res.users', string='Salesman', default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string='Buyer', copy=False)
    active = fields.Boolean(default=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=fields.Date.today() + relativedelta(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(selection=[
        ("north", "North"),
        ("south", "South"),
        ("east", "East"),
        ("west", "West")
    ])
    state = fields.Selection(selection=[
        ("new", "New"),
        ("offer received", "Offer Received"),
        ("offer accepted", "Offer Accepted"),
        ("sold", "Sold"),
        ("canceled", "Canceled")
    ], default="new")
