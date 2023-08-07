from odoo import models, fields, api
from odoo.exceptions import ValidationError

class module_state_pass(models.Model):
    _name = 'type_property.real_state'
    _description = 'Is an object about the information of saler and the house saled'
    _order = 'sequence'

    name = fields.Char(string="Name", required=True)
    prop_ids = fields.One2many('module_odoo.module_odoo_pass', 'type_property')
    sequence = fields.Integer()
    offer_ids = fields.One2many('offer_property.offer', 'property_type_id')
    offer_count = fields.Integer(compute ='_count_offer')

    @api.depends('offer_ids')
    def _count_offer(self):
        for record in self:
            record.offer_count = len(record.offer_ids)
    
    @api.onchange('name')
    def onchange_name (self):
        if isinstance(self.name, str) and self.name == self.name.lower(): 
            raise ValidationError ('Can not introduce numbers in tags, besides, the first letter for tag must be a uppercase. Please try again')