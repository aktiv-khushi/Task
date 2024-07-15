from datetime import date
from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    dob = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age", compute="_compute_age")

    @api.depends('dob')
    def _compute_age(self):
        for rec in self:
            if rec.dob:
                today = date.today()
                birth_date = fields.Date.from_string(rec.dob)
                rec.age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            else:
                rec.age = 0

