from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    operation_cee_id = fields.Many2one(
        'ibatix.operation.cee',
        string='Opération CEE',
    )
