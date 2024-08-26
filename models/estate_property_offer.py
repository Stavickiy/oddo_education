# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from dateutil.relativedelta import relativedelta

from odoo import fields, models, api


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
    create_date = fields.Date(copy=False, default=fields.Date.today())
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute='_compute_deadline_date', inverse='_inverse_validity_days')


    @api.depends('validity')
    def _compute_deadline_date(self):
        for record in self:
            if record.validity and (record.create_date + relativedelta(days=record.validity)) != record.date_deadline:
                record.date_deadline = record.create_date + relativedelta(days=record.validity)


    def _inverse_validity_days(self):
        for record in self:
            if record.date_deadline and (record.date_deadline - record.create_date).days != record.validity:
                record.validity = (record.date_deadline - record.create_date).days
