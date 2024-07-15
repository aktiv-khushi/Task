from odoo import models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    '''Combines the quantities of order lines with the same product in a sale order line.'''

    # def action_combine_sale_order(self):
    #     order_id = list(self.order_line)
    #     combined_orders = {}
    #     for rec in order_id:
    #         if rec.product_id in combined_orders:
    #             combined_orders[rec.product_id].product_uom_qty += rec.product_uom_qty
    #             rec.unlink()
    #         else:
    #             combined_orders[rec.product_id] = rec

    # Optimize

    def action_combine_sale_order(self):
        """
        Combines sale order lines with the same product by summing up their quantities.
        """
        combine_lines = {}
        for line in self.order_line:
            if line.product_id not in combine_lines:
                combine_lines[line.product_id] = line
            elif line.product_id in combine_lines:
                combine_lines[line.product_id].product_uom_qty += line.product_uom_qty
                line.unlink()


    # def action_combine_sale_order(self):
    #     combine_lines = {}
    #     for line in self.order_line:
    #         if line.product_id in combine_lines:
    #             combine_lines[line.product_id].product_uom_qty += line.product_uom_qty
    #             line.unlink()
    #         else:
    #             combine_lines[line.product_id] = line
