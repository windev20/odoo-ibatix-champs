from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    fiscal_ids = fields.One2many('ibatix.partner.fiscal', 'partner_id', string='Données fiscales')

    civilite = fields.Selection([
        ('monsieur', 'Monsieur'),
        ('madame', 'Madame'),
    ], string='Civilité')

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

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        if 'country_id' in fields_list and not res.get('country_id'):
            france = self.env.ref('base.fr', raise_if_not_found=False)
            if france:
                res['country_id'] = france.id
        return res
