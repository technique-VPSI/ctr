# -*- coding: utf-8 -*-

from odoo import models, fields


class ctr(models.Model):
    _inherit = 'helpdesk.ticket'
    numero_ticket = fields.Char(string="Numéro de ticket")
