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

    # def set_values(self):
    #     super(ResConfigSettings, self).set_values()
    #     param = self.env['ir.config_parameter'].sudo().set_param(
    #         'invoice_configuration.invoice_creation_option',
    #          self.invoice_creation_option)

    # @api.model
    # def get_values(self):
    #     res = super(ResConfigSettings, self).get_values()
    #     res.update(
    #         invoice_creation_option=self.env['ir.config_parameter']
    #         .sudo().get_param('invoice_configuration.invoice_creation_option')
    #     )
    #     return res
