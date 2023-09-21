from werkzeug import urls, utils
from odoo import http
from odoo.http import request
import logging
import werkzeug
logger = logging.getLogger(__name__)

from odoo.addons.payment.controllers.portal import PaymentProcessing
from odoo.addons.portal.controllers.portal import get_records_pager, pager as portal_pager, CustomerPortal

res_code = {
    0:'Pendiente',
    1:'Procesado',
    2:'En Proceso',
    3:'Cancelado',
}

class VenezuelaPaymentsControllers(http.Controller):

    @http.route(['/payment/venezuela/redirect'], auth='public', csrf=False)
    def redirect_to_venezuela(self, **post):
        url = post.get('x_relay_url',False)
        if url:
            return werkzeug.utils.redirect(url)
        else:
            raise werkzeug.exceptions.NotFound()

    @http.route(['/payment/venezuela/callback'], type='http', website=True, auth='public', csrf=False)
    def handle_venezuela_payments_callback_http(self, control=None, **post):
        tx = http.request.env['payment.transaction'].sudo().search([('acquirer_reference','=',post.get('id'))])
        status =  tx.venezuela_payments_callback()
        if status == 1:
            return request.render('payment.confirm', {'tx': tx, 'status': 'success', 'message': '<h3>Pago Confirmado<h3><br>'})
        elif status == 0:
            return request.render('payment.confirm', {'tx': tx, 'status': 'warning', 'message': '<h3>{message}<h3><br>'.format(message=res_code[status])})
        elif status == 2:
            return request.render('payment.confirm', {'tx': tx, 'status': 'warning', 'message': '<h3>{message}<h3><br>'.format(message=res_code[status])})
        elif status == 3:
            return request.render('payment.confirm', {'tx': tx, 'status': 'danger', 'message': '<h3>{message}<h3><br>'.format(message=res_code[status])})
        else:
            return werkzeug.utils.redirect("/shop/payment")