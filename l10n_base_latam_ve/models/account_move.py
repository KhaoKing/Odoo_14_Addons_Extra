# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = "account.move"

    street = fields.Char(readonly=True, string='Street')
    street2 = fields.Char(readonly=True, string='Street 2')
    phone_number = fields.Char(readonly=True, string='Phone Number')
    country_id = fields.Char(readonly=True, string='Country ID')
    vat = fields.Char(readonly=True, string='VAT')

    @api.onchange('partner_id')
    def _onchange_contact_info(self):
        partner_id = self.partner_id
        if partner_id:
            street = self.partner_id.street
            vat = self.partner_id._get_vat() 
            print (street)
            print (vat)   
            if not street or not vat:
                raise UserError ("Ops! This client doesn't have an Address or VAT defined. Check the information of Contact")
            self.write({
                'country_id': self.partner_id.country_id.id if self.partner_id.country_id else False,
                'street': street,
                'street2': self.partner_id.street2,
                'phone_number': self.partner_id.phone,
                'vat': vat,
            })


