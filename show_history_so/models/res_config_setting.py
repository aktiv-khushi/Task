from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    """res.config.settings add selection."""

    show_history_for_order = fields.Selection(
        [("draft", " Quotation State"), ("sale", "Sale Order State")],
        string="Show History for order",
        config_parameter="show_history_so.show_history_for_order",
    )
