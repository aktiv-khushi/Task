from odoo import models, fields, api


class SaleorderLine(models.Model):
    _inherit = 'sale.order.line'

    production_commission = fields.Float("Production commission", compute="_compute_production_commission", store=True)

    '''Computes the production commission for each sale order line and stores the result in the 'production_commission' field.'''

    @api.depends('order_id.sales_commission', 'price_unit')
    def _compute_production_commission(self):
        for rec in self:
            rec.production_commission = rec.price_unit * (rec.order_id.sales_commission / 100)
