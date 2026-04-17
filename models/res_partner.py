from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    revenu_fiscal = fields.Monetary(string='Revenu fiscal de référence', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id', readonly=True)
    nb_parts_foyer = fields.Integer(string='Nombre de parts dans le foyer')
    annee_fiscale = fields.Integer(string='Année fiscale')

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
