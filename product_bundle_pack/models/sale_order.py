from odoo import api, fields, models
# from odoo.fields import Command


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    product_pack_ids = fields.Many2many('product.template',
                                        string='Select Pack',
                                        domain=[('is_product_pack', '=', True)])

    def action_confirm(self):
        super().action_confirm()
        for line in self.order_line:
            if line.product_id.is_product_pack:
                for record in line.product_template_id.pack_products_ids:
                    for rec in self.picking_ids:
                        move = rec.move_ids.create({
                            'name': record.product_id.name,
                            'product_id': record.product_id.id,
                            'product_uom_qty': record.quantity * line.product_uom_qty,
                            'product_uom': record.product_id.uom_id.id,
                            'picking_id': rec.id,
                            'location_id': rec.location_id.id,
                            'location_dest_id': rec.location_dest_id.id,
                        })
                        move._action_confirm()

    # @api.onchange('product_pack_ids')
    # def onchange_product_pack_ids(self):
    #     if self.product_pack_ids:
    #         new_order_lines = []
    #         for rec in self.product_pack_ids:
    #             product_already_added = any(
    #                 line.product_id.id == rec._origin.id for line in
    #                 self.order_line)
    #             if not product_already_added:
    #                 new_order_lines.append((0, 0, {
    #                     'product_id': rec.id,
    #                     'name': rec.name,
    #                     'product_uom_qty': 1,
    #                     'price_unit': rec.pack_price,
    #                 }))
    #                 self.order_line = new_order_lines
    #     elif not self.product_pack_ids:
    #         self.order_line = [(5, 0, 0)]

