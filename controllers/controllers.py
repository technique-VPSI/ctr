# -*- coding: utf-8 -*-
# from odoo import http


# class Ctr(http.Controller):
#     @http.route('/ctr/ctr/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ctr/ctr/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ctr.listing', {
#             'root': '/ctr/ctr',
#             'objects': http.request.env['ctr.ctr'].search([]),
#         })

#     @http.route('/ctr/ctr/objects/<model("ctr.ctr"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ctr.object', {
#             'object': obj
#         })
