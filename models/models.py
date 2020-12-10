# -*- coding: utf-8 -*-

from odoo import models, fields, api


 class ctr(models.Model):
     _name = 'ctr.ctr'
     _inherit="helpdesk.ticket"

     numero_ticket = fields.Char(string="Numéro de ticket")
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
