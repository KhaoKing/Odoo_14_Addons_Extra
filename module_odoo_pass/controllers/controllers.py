# -*- coding: utf-8 -*-
# from odoo import http


# class ModuleOdooPass(http.Controller):
#     @http.route('/module_odoo_pass/module_odoo_pass/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module_odoo_pass/module_odoo_pass/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module_odoo_pass.listing', {
#             'root': '/module_odoo_pass/module_odoo_pass',
#             'objects': http.request.env['module_odoo_pass.module_odoo_pass'].search([]),
#         })

#     @http.route('/module_odoo_pass/module_odoo_pass/objects/<model("module_odoo_pass.module_odoo_pass"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module_odoo_pass.object', {
#             'object': obj
#         })
