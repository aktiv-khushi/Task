from odoo import models, fields


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    state = fields.Selection(
        selection_add=[("append", "Append")], string="Status", readonly=True
    )

    dis_related = fields.Float(related="partner_id.discount")

    def append_action(self):
        self.write({"state": "append"})

    def confirm_append_action(self):
        self.write({"state": "purchase"})

    """compute method to get total field add discount."""

    def _compute_tax_totals(self):
        res = super(PurchaseOrder, self)._compute_tax_totals()
        discount = self.dis_related
        if discount:
            total = self.tax_totals["amount_untaxed"]
            self.tax_totals["amount_untaxed"] = (
                total - (total * discount) / 100
            )
        return res
