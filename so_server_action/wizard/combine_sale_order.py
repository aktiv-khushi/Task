from odoo import fields, models


class CombineCustomer(models.TransientModel):
    _name = "combine.customer"

    order_ids = fields.Many2many("sale.order", readonly=1)

    """when user clicks on this button the chosen quotation should be
     merged into single quotation along with the lines
    and others should be deleted."""

    def combine_customer_and_lines(self):
        sale_obj = self.env["sale.order"]
        active_ids = self.env.context.get("active_ids")
        sale_orders = sale_obj.browse(active_ids)
        combine_order = sale_obj.create(
            {"partner_id": self.selected_orders[0].partner_id.id}
        )
        for order in sale_orders:
            for line in order.order_line:
                line.copy(default={"order_id": combine_order.id})
            order.unlink()
