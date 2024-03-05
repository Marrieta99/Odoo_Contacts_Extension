from odoo import models, fields, api


class Partner(models.Model):
    _description = "Contact"
    _inherit = "res.partner"

    industry_id = fields.Many2one('res.partner.industry', 'Category')

    segment_id = fields.Many2one(
        string="Segmento",
        comodel_name="segmento"
    )
