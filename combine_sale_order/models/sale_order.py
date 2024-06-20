from odoo import models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    '''Combines the quantities of order lines with the same product in a sale order line.'''

    def action_combine_sale_order(self):
        print('server action')
        order_id = list(self.order_line)
        combined_orders = {}
        for rec in order_id:
            if rec.product_id in combined_orders:
                combined_orders[rec.product_id].product_uom_qty += rec.product_uom_qty
                rec.unlink()
            else:
                combined_orders[rec.product_id] = rec
