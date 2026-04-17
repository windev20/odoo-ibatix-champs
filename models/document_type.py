from odoo import fields, models


class IbatixDocumentType(models.Model):
    _name = 'ibatix.document.type'
    _description = 'Type de document IBATIX'
    _order = 'name'

    name = fields.Char(string='Nom', required=True)

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Ce nom de document existe déjà.'),
    ]
