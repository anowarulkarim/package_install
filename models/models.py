# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class package_install(models.Model):
#     _name = 'package_install.package_install'
#     _description = 'package_install.package_install'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

