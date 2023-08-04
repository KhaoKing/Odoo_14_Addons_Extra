# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime 
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError


class module_odoo_pass(models.Model):
    _name = 'module_odoo.module_odoo_pass'
    _description = 'This is my first odoo community module, learning how it works'
    _order = 'id desc'

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Available From" ,copy=False , default=lambda self: (datetime.now() + relativedelta(months=3)))
    expected_price = fields.Float(string="Expected Price",required=True)
    selling_price = fields.Float(string="Selling Price",readonly=True, copy=False)
    bedrooms = fields.Integer(string="Bedrooms", default=2)
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area (sqm)")
    garden_orentation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('west', 'West'),
        ('east', 'East')], string="Garden Orientation")
    active = fields.Boolean(default=True)
    state = fields.Selection([
        ('new','New'),
        ('offer_received','Offer Received'),
        ('offer_accepted','Offer Accepted'),
        ('sold','Sold'),
        ('canceled','Canceled')], required=True, copy=False, default="new")
    type_property = fields.Many2one('type_property.real_state', string='Property Type')
    tag_property = fields.Many2many('tag_property.state', 'tag_id')
    salesman = fields.Many2one('res.users',string='Seller', index=True, tracking=True, default=lambda self: self.env.user)
    buyer = fields.Many2one('res.users',string='Buyer', copy=False)
    offer_ids = fields.One2many('offer_property.offer', 'property_id', string='Offers Ids')
    total_area = fields.Float(compute="_sum_area")
    best_price = fields.Float(string="Best Offer", compute="_better_offer")
    color = fields.Integer()
    
    
    @api.depends("total_area")
    def _sum_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids.offer_price")
    def _better_offer(self):
        for record in self:
            better_offer = record.offer_ids.mapped('offer_price')
            record.best_price = max(better_offer) if better_offer else 0.0

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_orentation = 'north'
            self.garden_area = 10.0
        else:
            self.garden_area = False
            self.garden_orentation = False

    def button_change_sold(self):
        if self.state == 'canceled':
            raise UserError ('The offer for this property is closed, for that, could be not selled')
        else:
            self.state = 'sold'

    def button_change_canceled(self):
        if self.state == 'sold':
            raise UserError ('The property it was sold, for that, could be not close the offer')
        else:
            self.state = 'canceled'

    _sql_constraints = [
        ("check_expected_price", "CHECK(expected_price > 0)", "Ops! The price you got enter, is wrong.  Please enter a price positive"),
    ]