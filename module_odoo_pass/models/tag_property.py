from odoo import models, fields, api
from odoo.exceptions import ValidationError

class tag_property_state_v(models.Model):
    _name = 'tag_property.state'
    _description = "Is an object about the information of the tag at home sales"

    name = fields.Char(required=True)
    
    @api.onchange('name')
    def onchange_name (self):
        if self.name and isinstance(self.name, str):
            self.name = self.name.lower()
            raise ValidationError ('This property is al ready, please enter another one')

