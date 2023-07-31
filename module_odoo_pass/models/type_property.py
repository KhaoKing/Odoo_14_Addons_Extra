from odoo import models, fields

class module_state_pass(models.Model):
    _name = 'type_property.real_state'
    _description = 'Is an object about the information of saler and the house saled'

    name = fields.Char(string="Name")