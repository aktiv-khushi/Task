from odoo import models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    """If price_unit is changed then longnotes appear with user name,
    product name and new price unit."""

    def write(self, vals):
        record = self.order_id
        if "price_unit" in self:
            record.message_post(
                body=f"{record.user_id.name} updated the Unit price for "
                     f"{self.product_id.name} to {self.price_unit}"
            )
            return super(PurchaseOrderLine, self).write(vals)
