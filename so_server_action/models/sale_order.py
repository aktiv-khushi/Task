from odoo import models, api
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    """server action throw wizard open"""

    @api.model
    def action_combine(self):
        active_ids = self.env.context.get("active_ids")
        selected_orders = self.env["sale.order"].browse(active_ids)
        customer_ids = set(order.partner_id.id for order in selected_orders)
        if len(customer_ids) != 1:
            raise ValidationError(
                "Selected orders have different customers."
                "Combining is not allowed."
            )
        return {
            "name": "Combine",
            "view_mode": "form",
            "type": "ir.actions.act_window",
            "views": [
                (
                    self.env.ref(
                        "so_server_action.combine_customer_form_view"
                    ).ids,
                    "form",
                )
            ],
            "res_model": "combine.customer",
            "res_id": False,
            "target": "new",
            "context": {"default_order_ids": self._context.get("active_ids")},
        }
