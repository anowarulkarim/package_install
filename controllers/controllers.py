# -*- coding: utf-8 -*-
# from odoo import http


# class PackageInstall(http.Controller):
#     @http.route('/package_install/package_install', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/package_install/package_install/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('package_install.listing', {
#             'root': '/package_install/package_install',
#             'objects': http.request.env['package_install.package_install'].search([]),
#         })

#     @http.route('/package_install/package_install/objects/<model("package_install.package_install"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('package_install.object', {
#             'object': obj
#         })

