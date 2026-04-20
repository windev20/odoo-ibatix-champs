from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    partner_badges_html = fields.Html(
        compute='_compute_partner_badges_html',
        store=False,
        sanitize=False,
    )

    @api.depends(
        'partner_id',
        'partner_id.is_company',
        'partner_id.categorie_precarite',
        'partner_id.categorie_mpr',
    )
    def _compute_partner_badges_html(self):
        PRECARITE = {
            'precaire': ('#dc3545', 'white', 'CEE · Précaire'),
            'modeste':  ('#fd7e14', 'white', 'CEE · Modeste'),
            'classique':('#6c757d', 'white', 'CEE · Classique'),
        }
        MPR_COLOR = {
            'bleu':   ('#0d6efd', 'white', 'MPR · Bleu'),
            'jaune':  ('#ffc107', '#212529', 'MPR · Jaune'),
            'violet': ('#6f42c1', 'white',   'MPR · Violet'),
            'rose':   ('#d63384', 'white',   'MPR · Rose'),
        }

        def badge(label, bg, color='white'):
            return (
                f'<span style="display:inline-block;padding:3px 10px;border-radius:20px;'
                f'background-color:{bg};color:{color};font-size:0.78rem;font-weight:600;'
                f'white-space:nowrap;">{label}</span>'
            )

        for order in self:
            p = order.partner_id
            if not p:
                order.partner_badges_html = False
                continue

            parts = []

            # Professionnel / Particulier
            if p.is_company:
                parts.append(badge('&#128188; Professionnel', '#0d6efd'))
            else:
                parts.append(badge('&#128100; Particulier', '#198754'))

            # Catégorie CEE précarité
            if p.categorie_precarite in PRECARITE:
                bg, fg, label = PRECARITE[p.categorie_precarite]
                parts.append(badge(label, bg, fg))

            # Catégorie MPR
            if p.categorie_mpr in MPR_COLOR:
                bg, fg, label = MPR_COLOR[p.categorie_mpr]
                parts.append(badge(label, bg, fg))

            order.partner_badges_html = (
                '<div style="display:flex;flex-wrap:wrap;gap:6px;padding:4px 0 6px 0;">'
                + ''.join(parts)
                + '</div>'
            )
