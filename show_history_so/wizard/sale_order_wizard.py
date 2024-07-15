from odoo import models, fields, api


class SaleOrderWizad(models.TransientModel):
    _name = "sale.order.wizard"

    name = fields.Many2one("res.partner", string="Name")
    product_id = fields.Many2one(
        "_product.template", string="Product", readonly=True
    )
    order_line_ids = fields.Many2many(comodel_name="sale.order.line")

    """ show all the Sale Order (state will be based
        on the Config settings) which will belong to Customer A and
        contains Product A in the Sale Order Line."""

    # @api.model
    # def default_get(self, fields_list):
    #     sale_order_line_id = self.env.context.get("active_id")
    #     record = self.env["sale.order.line"].browse(sale_order_line_id)
    #     res = super().default_get(fields_list)
    #     res["name"] = record.order_id.partner_id
    #     res["product"] = record.product_template_id
    #     show_history = self.env["ir.config_parameter"].get_param(
    #         "show_history_so.show_history_for_order"
    #     )
    #     store_records = self.env["sale.order.line"].search(
    #         [
    #             ("order_id.partner_id.name", "=", res["name"].name),
    #             ("product_template_id.name", "=", res["product"].name),
    #             ("order_id.state", "=", show_history),
    #         ]
    #     )
    #     res.update(
    #         {
    #             "order_line_ids": [
    #                 (
    #                     fields.Command.set(
    #                         [int(record) for record in store_records]
    #                     )
    #                 )
    #             ]
    #         }
    #     )
    #     return res

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        sale_order_line_id = self.env.context.get("active_id")
        if sale_order_line_id:
            record = self.env["sale.order.line"].browse(sale_order_line_id)
            res.update({'name': record.order_id.partner_id, 'product': record.product_template_id})
            res["order_line_ids"] = [(6, 0, self.env["sale.order.line"].search([
                ("order_id.partner_id", "=", res["name"]),
                ("product_template_id", "=", res["product"]),
                ("order_id.state", "=", self.env["ir.config_parameter"].get_param(
                    "show_history_so.show_history_for_order"))]))]
        return res

