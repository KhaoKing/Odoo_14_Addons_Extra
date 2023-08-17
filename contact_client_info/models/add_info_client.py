# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = "account.move"

    street = fields.Char(readonly=True)
    street2 = fields.Char(readonly=True)
    phone_number = fields.Char(readonly=True)
    country_id = fields.Char(readonly=True)
    vat = fields.Char(readonly=True)

    @api.onchange('partner_id')
    def _onchange_contact_info(self):
        if self.partner_id:
            country_id_partner = self.partner_id.country_id
            self.street = self.partner_id.street
            self.street2 = self.partner_id.street2
            self.phone_number = self.partner_id.phone
            self.country_id = country_id_partner.id if country_id_partner else False
            self._get_vat()

    def _get_vat(self):
        vat_aux = self.partner_id.l10n_latam_identification_type_id.name + self.partner_id.vat
        self.vat = vat_aux if vat_aux != 0 else ''
