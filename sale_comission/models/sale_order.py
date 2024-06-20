from odoo import models, fields


class Saleorder(models.Model):
    _inherit = 'sale.order'

    sales_commission = fields.Float("Sales Commission", default=2.5)
