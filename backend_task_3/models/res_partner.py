from odoo import models, fields


class Contacts(models.Model):
    _inherit = "res.partner"

    discount = fields.Float("Discount")
