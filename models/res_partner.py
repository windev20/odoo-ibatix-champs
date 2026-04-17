from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    categorie_precarite = fields.Selection([
        ('precaire', 'Précaire'),
        ('modeste', 'Modeste'),
        ('classique', 'Classique'),
    ], string='Catégorie CEE')
