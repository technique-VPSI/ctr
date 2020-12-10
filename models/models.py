# -*- coding: utf-8 -*-

from odoo import models, fields


class ctr(models.Model):
    _name = 'ctr.ctr'
    _inherit = 'helpdesk.ticket'
    numero_ticket = fields.Char(string="Numéro de ticket")
