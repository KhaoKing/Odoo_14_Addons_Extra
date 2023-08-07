from odoo import models, fields

class inherit_res_user(models.Model):
    _inherit = 'res.partner'

    property_ids = fields.One2many('module_odoo.module_odoo_pass', 'salesman', string = 'Properties per Seller')