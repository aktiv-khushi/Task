from odoo import models, fields
from odoo.exceptions import ValidationError


class StockPicking(models.Model):
    _inherit = "stock.picking"

    shipping_hold = fields.Boolean("shipping hold")

    """If sipping hold is true and click on button validate
    in stock.picking shows validation error."""

    def button_validate(self):
        if self.shipping_hold:
            raise ValidationError(
                f"This stock movement is currently on Shipping Hold."
                f"Its associated Sales Order {self.sale_id.name}"
                f"must be taken off hold before it can be validated."
            )
        return super().button_validate()
