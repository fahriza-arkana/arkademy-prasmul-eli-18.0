# -*- coding: utf-8 -*-
# from odoo import http


# class FahrizaLibrary(http.Controller):
#     @http.route('/fahriza_library/fahriza_library', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fahriza_library/fahriza_library/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fahriza_library.listing', {
#             'root': '/fahriza_library/fahriza_library',
#             'objects': http.request.env['fahriza_library.fahriza_library'].search([]),
#         })

#     @http.route('/fahriza_library/fahriza_library/objects/<model("fahriza_library.fahriza_library"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fahriza_library.object', {
#             'object': obj
#         })

