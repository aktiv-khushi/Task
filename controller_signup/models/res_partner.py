from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    dob = fields.Datetime("Date Of Birth")
    pob = fields.Char("Place of Birth")
    gender = fields.Selection([("male", "Male"), ("female", "Female"), ("other", "Other")], string="Gender")
    passport = fields.Char("Passport")
    license = fields.Char("Driving License")
    language = fields.Selection([('hindi', 'Hindi'), ('gujarati', 'gujarati'), ('eng', 'English')],
                                string="Specking Language", widget="radio")
    status = fields.Selection([("single", "Single"), ("married", "Married")], string="Marital Status")
