from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    invoice_creation_option = fields.Selection(
        [
            ("sale", "Sale"),
            ("purchase", "Purchase"),
            ("sale_purchase", "Sale & Purchase"),
        ],
        string="Invoice Creation Option",
        config_parameter="invoice_configuration.invoice_creation_option",
    )

