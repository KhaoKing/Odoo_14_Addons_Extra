from odoo import models, fields, api
from odoo.exceptions import ValidationError

class module_state_pass(models.Model):
    _name = 'type_property.real_state'
    _description = 'Is an object about the information of saler and the house saled'

    name = fields.Char(string="Name")
    prop_ids = fields.One2many('module_odoo.module_odoo_pass', 'property_ids')
    

    @api.onchange('name')
    def onchange_name (self):
        if self.name and isinstance(self.name, str):
            self.name = self.name.lower()
            raise ValidationError ('This tag is al ready, please enter another one')
