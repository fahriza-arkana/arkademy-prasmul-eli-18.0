# -*- coding: utf-8 -*-
# from odoo import http


# class IrvanLibrary(http.Controller):
#     @http.route('/irvan_library/irvan_library', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/irvan_library/irvan_library/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('irvan_library.listing', {
#             'root': '/irvan_library/irvan_library',
#             'objects': http.request.env['irvan_library.irvan_library'].search([]),
#         })

#     @http.route('/irvan_library/irvan_library/objects/<model("irvan_library.irvan_library"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('irvan_library.object', {
#             'object': obj
#         })

