# -*- coding: utf-8 -*-

from odoo import models, fields, api


class odoo_olamundo_samuel(models.Model):
    _name = 'odoo_olamundo_samuel.olamundo'
    _description = 'Exemplo olamundo'

    name = fields.Char(string="Hola mundo:")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
