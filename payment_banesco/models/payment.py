# -*- coding: utf-8 -*-
from werkzeug import urls
from odoo.http import request
import hashlib
import hmac
import logging
import time
import requests
import json
from unicodedata import normalize

from odoo import _, api, fields, models
from odoo.addons.payment.models.payment_acquirer import ValidationError
from odoo.tools.float_utils import float_compare, float_repr
from odoo.exceptions import UserError

logger = logging.getLogger(__name__)
TIMEOUT = 30

def _get_token(id,key,url):
    token = False
    data = {
        'grant_type':'client_credentials',
        'client_id':id,
        'client_secret':key,
        'Content-Type': 'application/json',
        'Cache-Control': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*'
        }
    try:
        res = requests.post(url, data, timeout=60)
        token = json.loads(res.content)['access_token']
    except requests.exceptions.Timeout:
        raise UserError(_('Timeout: el servidor no ha respondido en 60s'))
    except (ValueError, requests.exceptions.ConnectionError):
        raise UserError(_('Servidor inaccesible, inténtelo más tarde'))
    return token

class PaymentAcquirerBanesco(models.Model):
    _inherit = 'payment.acquirer'

    provider = fields.Selection(selection_add=[('banesco', 'Banesco')], ondelete={'banesco': 'set default'})
    banesco_transaction_key = fields.Char(string='API Key', groups='base.group_user')
    banesco_signature_key = fields.Char(string='API Secret',groups='base.group_user')