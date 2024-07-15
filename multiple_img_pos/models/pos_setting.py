from odoo import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    multi_image = fields.Boolean(string='Multi Image',
                                 help="Allow Multiple image of products")
