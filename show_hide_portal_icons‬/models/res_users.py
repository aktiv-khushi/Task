from odoo import models, fields


class ResUsers(models.Model):
    _inherit = "res.users"

    project_section_hidden = fields.Boolean(string="Hide Project Sections")
