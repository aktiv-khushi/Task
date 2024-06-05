from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    signup_process = fields.Boolean("Signup Process", config_parameter="controller_signup.process")
