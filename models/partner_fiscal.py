from odoo import fields, models


class IbatixPartnerFiscal(models.Model):
    _name = 'ibatix.partner.fiscal'
    _description = 'Données fiscales partenaire IBATIX'
    _order = 'annee_fiscale desc'

    partner_id = fields.Many2one('res.partner', required=True, ondelete='cascade')
    numero_fiscal = fields.Char(string='Numéro Fiscal')
    reference_fiscal = fields.Char(string='Référence Fiscal')
    annee_fiscale = fields.Integer(string='Année fiscale')
    revenu_fiscal = fields.Monetary(string='Revenu fiscal de référence', currency_field='currency_id')
    currency_id = fields.Many2one(
        'res.currency',
        related='partner_id.company_id.currency_id',
        readonly=True,
        store=True,
    )
    nb_parts_foyer = fields.Integer(string='Nombre de parts dans le foyer')
    avis_imposition = fields.Binary(string="Avis d'imposition", attachment=True)
    avis_imposition_filename = fields.Char(string="Nom du fichier avis")
