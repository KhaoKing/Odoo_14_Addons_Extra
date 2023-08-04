from odoo import models, fields, api
from odoo.exceptions import ValidationError

class tag_property_state_v(models.Model):
    _name = 'tag_property.state'
    _description = "Is an object about the information of the tag at home sales"
    _order = 'name'

    name = fields.Char(required=True)
    color = fields.Integer()
    
    @api.onchange('name')
    def onchange_name (self):
        if isinstance(self.name, str) and self.name == self.name.lower(): 
            raise ValidationError ('Can not introduce numbers in tags, besides, the first letter for tag must be a uppercase. Please try again')
