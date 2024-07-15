from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    bulk_product_template = fields.Many2one(
        'bulk.product', string="Bulk Product Template")

    '''Once you select the record than all the products which
    are in bulk products of model
    bulk product should be listed in Sale Order Line with qty as 1.'''

    # @api.onchange('bulk_product_template')
    # def _onchange_bulk_product(self):
    # if self.bulk_product_template:
    #     self.order_line = [(5, 0, 0)]
    #     order_lines = []
    #     for line in self.bulk_product_template.bulk_products:
    #         order_lines.append((0, 0, {
    #             'product_id': line.product_id.id,
    #             'product_uom_qty': 1
    #         }))
    #     self.order_line = order_lines

    # Optimize

    '''Once you select the record than all the products which
        are in bulk products of model
        bulk product should be listed in Sale Order Line with qty as 1.'''

    @api.onchange('bulk_product_template')
    def _onchange_bulk_product(self):
        if self.bulk_product_template:
            self.order_line = [(5, 0, 0)]
            self.order_line = [(0, 0, {
                'product_id': line.product_id.id,
                'product_uom_qty': 1
            }) for line in self.bulk_product_template.bulk_products]
