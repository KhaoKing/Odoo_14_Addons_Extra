from odoo import models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    def _get_vat(self):
        name = []
        type_id = self.l10n_latam_identification_type_id
        vat = self.vat
        if type_id and vat:
            name.append(type_id.name)
            name.append(vat)
        return ''.join(name)
# Recuerda, []= Lista, {} = Diccionario , () = Tupla