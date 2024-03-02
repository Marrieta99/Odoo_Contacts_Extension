from odoo import models, fields


class Segmento(models.Model):
    _name = "segmento"  # minimo requerido
    _description = "Segmento"  # minimo requerido
    _order = "id desc"

    _sql_constraints = [
        ("name_uniq", "unique(name)", "El nombre del segmento debe ser único")
    ]

    name = fields.Char("Nombre del Segmento", required=True)
    description = fields.Text("Descripcion del segmento")
    contact_ids = fields.One2many(
        string="Contactos",
        comodel_name="res.partner",
        inverse_name="segment_id"
    )