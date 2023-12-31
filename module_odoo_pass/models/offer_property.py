from odoo import models, fields, api, _
from datetime import timedelta
from odoo.exceptions import ValidationError, UserError

class offer_property_class(models.Model):
    _name = 'offer_property.offer'
    _description = 'It is an object which will have the record of the offers'
    # _order = 'offer_price desc' 

    offer_price = fields.Float()
    status_offer = fields.Selection([
        ('accepted','Accepted'),
        ('refused','Refused')], copy=False)
    buyer_user = fields.Many2one('res.partner', 'Partners', required=True)
    property_id = fields.Many2one('module_odoo.module_odoo_pass')
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute='_sum_date_deadline', inverse="_inverse_sum_date_deadline", store=True)
    property_type_id = fields.Many2one (related='property_id.type_property', store=True)

    @api.depends('validity')
    def _sum_date_deadline(self):
        create_date = fields.Date.context_today(self)
        for record in self:        
            if record.validity:
                record.date_deadline = create_date + timedelta(days=record.validity)

    def _inverse_sum_date_deadline(self):
        create_date = fields.Date.context_today(self)
        for record in self:        
            if record.date_deadline and create_date:
                record.validity = (record.date_deadline - create_date).days

    def accepted_value_state_offer(self):
        for record in self:    
            if record.offer_price < 0.9*record.property_id.expected_price:
                raise ValidationError ("Ops! Your offer has been declined. Must apply with 90% of the expected price to become accepted")
            else:
                self.status_offer = 'accepted'
                self.property_id.buyer = self.buyer_user
                self.property_id.selling_price = self.offer_price
                self.property_id.state = 'offer_accepted'

    def canceled_value_state_offer(self):
        self.status_offer = 'refused'
        self.property_id.buyer = False
        self.property_id.selling_price = False
        self.property_id.state = 'new'

    _sql_constraints = [
        ("check_offer_price", "CHECK(offer_price > 0.0)", "Ops! The price you got enter, is wrong.  Please enter a price positive"),
    ]

    @api.model
    def create (self, vals):
        stats_offers = vals.get('status_offer')
        stats_property = vals.get('property_id')
        stats_model_real = self.env['module_odoo.module_odoo_pass'].browse(stats_property)
        review_price_offers = self.search([("property_id",'=', stats_property)], order = "offer_price desc", limit = 1)
        stats_price = vals.get('offer_price')

        if stats_offers == False:
            stats_model_real.state = 'offer_received'

        if review_price_offers and stats_price < review_price_offers.offer_price:
            raise UserError('Ups! Sorry, you can not introduce an offer lower than %s' %stats_model_real.best_price)       

        return super(offer_property_class, self).create(vals)