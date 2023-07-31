from odoo import models, fields

class tag_property_state_v(models.Model):
    _name = 'tag_property.state'
    _description = "Is an object about the information of the tag at home sales"

    name = fields.Char(required=True)