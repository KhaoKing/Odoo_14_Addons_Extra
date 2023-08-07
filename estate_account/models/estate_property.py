from odoo import models, api

class estate_account(models.Model):
    _inherit = 'module_odoo.module_odoo_pass'

    def button_change_sold (self):
        bill_payment = super(estate_account, self).button_change_sold()

        return bill_payment()