from odoo import fields, models


class IbatixPartnerDocument(models.Model):
    _name = 'ibatix.partner.document'
    _description = 'Document partenaire IBATIX'
    _order = 'date desc, id desc'

    partner_id = fields.Many2one('res.partner', required=True, ondelete='cascade')
    document_type_id = fields.Many2one('ibatix.document.type', string='Nom', required=True)
    file = fields.Binary(string='Documents', attachment=True)
    filename = fields.Char(string='Nom du fichier')
    date = fields.Date(string='Date', default=fields.Date.today)
