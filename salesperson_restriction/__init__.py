# -*- coding: utf-8 -*-
# # from . import models
import odoo.api as api
from odoo.api import SUPERUSER_ID

def desactivate_rule(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})  
    rule = env['ir.rule'].search([('name', '=', 'res.partner.rule.private.employee')])
    rule.write({'active': False})

def uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})  
    rule = env['ir.rule'].search([('name', '=', 'res.partner.rule.private.employee')])
    rule.write({'active': True})