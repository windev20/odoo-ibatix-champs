from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    fiscal_ids = fields.One2many('ibatix.partner.fiscal', 'partner_id', string='Données fiscales')

    categorie_precarite = fields.Selection([
        ('precaire', 'Précaire'),
        ('modeste', 'Modeste'),
        ('classique', 'Classique'),
    ], string='Catégorie CEE')

    categorie_mpr = fields.Selection([
        ('bleu', '🔵  Bleu'),
        ('jaune', '🟡  Jaune'),
        ('violet', '🟣  Violet'),
        ('rose', '🩷  Rose'),
    ], string='Catégorie MPR')

    document_ids = fields.One2many('ibatix.partner.document', 'partner_id', string='Documents')
