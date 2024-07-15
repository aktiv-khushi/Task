from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    shipping_hold = fields.Boolean("Shipping Hold")

    """If shipping hold is active in sale.order and not in done state
    then shipping hold is automatically active in stock.picking."""

    def action_confirm(self):
        res = super().action_confirm()
        # if self.shipping_hold:
        for record in self.picking_ids:
            if record.state != "done":
                record.shipping_hold = self.shipping_hold

        return res

    def write(self, vals):
        res = super().write(vals)
        # if self.shipping_hold == True:
        records = self.picking_ids
        for record in records:
            if record.state != "done":
                record.shipping_hold = self.shipping_hold
        return res

    # optimize

    """If shipping hold is active in sale.order and not in done state
        then shipping hold is automatically active in stock.picking."""
    def action_confirm(self):
        res = super().action_confirm()
        if self.shipping_hold:
            self.picking_ids.filtered(lambda r: r.state != "done").write({
                'shipping_hold': self.shipping_hold})
        return res

    def write(self, vals):
        res = super().write(vals)
        if 'shipping_hold' in vals:
            self.picking_ids.filtered(lambda r: r.state != "done").write({
                'shipping_hold': vals['shipping_hold']})
        return res

