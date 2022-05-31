# -*- coding: utf-8 -*-
# from odoo import http


# class OdooOlamundoSamuel(http.Controller):
#     @http.route('/odoo_olamundo_samuel/odoo_olamundo_samuel/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_olamundo_samuel/odoo_olamundo_samuel/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_olamundo_samuel.listing', {
#             'root': '/odoo_olamundo_samuel/odoo_olamundo_samuel',
#             'objects': http.request.env['odoo_olamundo_samuel.odoo_olamundo_samuel'].search([]),
#         })

#     @http.route('/odoo_olamundo_samuel/odoo_olamundo_samuel/objects/<model("odoo_olamundo_samuel.odoo_olamundo_samuel"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_olamundo_samuel.object', {
#             'object': obj
#         })
