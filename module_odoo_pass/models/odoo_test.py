# -*- coding: utf-8 -*-
from odoo import models, fields


class module_odoo_pass(models.Model):
    _name = 'module_odoo.module_odoo_pass'
    _description = 'This is my first odoo community module, learning how it works'

    name = fields.Char(required='True')
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy="False", default=fields.Date.today())
    expected_price = fields.Float(required='True')
    selling_price  = fields.Float(readonly='True', copy="False")
    bedrooms  = fields.Integer(default=2)
    living_area  = fields.Integer()
    facades  = fields.Integer()
    garage  = fields.Boolean()
    garden  = fields.Boolean()
    garden_area  = fields.Integer()
    garden_orentation  = fields.Selection([('North', 'North'), 
                                            ('South', 'South'),
                                            ('West', 'West'),
                                            ('East', 'East')])
    
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
