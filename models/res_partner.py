from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

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
