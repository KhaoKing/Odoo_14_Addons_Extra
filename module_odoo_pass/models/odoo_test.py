# -*- coding: utf-8 -*-
from odoo import models, fields
from datetime import datetime 
from dateutil.relativedelta import relativedelta


class module_odoo_pass(models.Model):
    _name = 'module_odoo.module_odoo_pass'
    _description = 'This is my first odoo community module, learning how it works'

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Available From" ,copy=False , default=lambda self: (datetime.now() + relativedelta(months=3)))
    expected_price = fields.Float(string="Expected Price",required=True)
    selling_price  = fields.Float(string="Selling Price",readonly=True, copy=False)
    bedrooms  = fields.Integer(string="Bedrooms", default=2)
    living_area  = fields.Integer(string="Living Area (sqm)")
    facades  = fields.Integer(string="Facades")
    garage  = fields.Boolean(string="Garage")
    garden  = fields.Boolean(string="Garden")
    garden_area  = fields.Integer(string="Garden Area (sqm)")
    garden_orentation  = fields.Selection([('North', 'North'), 
                                            ('South', 'South'),
                                            ('West', 'West'),
                                            ('East', 'East')], string="Garden Orientation")
    active = fields.Boolean(default=True)
    state = fields.Selection([('new','New'),
                            ('offer received','Offer Received'),
                            ('offer acepted','Offer Acepted'),
                            ('sold','Sold'),
                            ('canceled','Canceled')], required=True, copy=False, default="new")
    type_property = fields.Many2one('type_property.real_state', string='Property Type')
    tag_property = fields.Many2many('tag_property.state', 'property_id')
    
    
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
