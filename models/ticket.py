# -*- coding: utf-8 -*-

from odoo import models, fields


class ctr(models.Model):
    _inherit = 'helpdesk.ticket'
    numero_ticket = fields.Char(string="Numéro de ticket")
    reference=fields.Char(string="Réference")
    objet_reclamation=fields.Char(string="Objet de la reclamation")
    date_reclamation=fields.Date(string="Date de raclamation")
    date_proch_action=fields.Date(string="Date de prochain action")

class product(models.Model):
    _inherit= 'helpdesk.ticket'
    code_produit=fields.Char(string='Code')
    libelle_produit=fields.Char(string='Produit')

class marque(models.Model):
    _inherit= 'helpdesk.ticket'
    code_marque=fields.Char(string='Code')
    libelle_marque=fields.Char(string='Marque')