# -*- coding: utf-8 -*-
from odoo import models, fields, api
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
    tag_property = fields.Many2many('tag_property.state', 'tag_id')
    salesman = fields.Many2one('res.users',string='Seller', index=True, tracking=True, default=lambda self: self.env.user)
    buyer = fields.Many2one('res.users',string='Buyer', copy=False)
    offer_ids = fields.One2many('offer_property.offer', 'property_id', string='Offers Ids')
    total_area = fields.Float(compute="_sum_area")
    best_price = fields.Float(string="Best Offer", compute="_better_offer")
    

    @api.depends("total_area")
    def _sum_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids.price")
    def _better_offer(self):
        for record in self:
            better_offer = record.offer_ids.mapped('price')
            record.best_price = max(better_offer) if better_offer else 0.0

    
