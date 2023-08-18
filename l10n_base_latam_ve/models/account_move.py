# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = "account.move"

    street = fields.Char(readonly=True)
    street2 = fields.Char(readonly=True)
    phone_number = fields.Char(readonly=True)
    country_id = fields.Char(readonly=True)
    vat = fields.Char(readonly=True)

    @api.onchange('partner_id')
    def _onchange_contact_info(self):
        if self.partner_id.street and self.partner_id.vat == '':
            raise UserError ('Este usuario no dispone de un RIF ni de alguna direccion, revise el contacto.')
        else:
            if self.partner_id:
                self.write({
                    'country_id': self.partner_id.country_id.id if self.partner_id.country_id else False,
                    'street': self.partner_id.street,
                    'street2': self.partner_id.street2,
                    'phone_number': self.partner_id.phone,
                    'vat': self.partner_id._get_vat(),
                })


