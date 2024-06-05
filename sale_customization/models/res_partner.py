from odoo import models, api
from odoo.osv import expression


class ResPartner(models.Model):
    _inherit = "res.partner"

    """See the customer's name along with his reference."""

    @api.depends("city", "name")
    def _compute_display_name(self):
        if self._context.get("sale_order"):
            for report in self:
                city = report.city
                report.display_name = f"{report.name} - {city}"
        else:
            super()._compute_display_name()

    """The customer should be searched with his references."""

    @api.model
    def _name_search(
        self, name, domain=None, operator="ilike", limit=None, order=None
    ):
        domain = domain or []
        if operator != "ilike" or (name or "").strip():
            name_domain = [
                "|",
                ("name", "ilike", name),
                ("city", "ilike", name),
            ]
            domain = expression.AND([name_domain, domain])
        return self._search(domain, limit=limit, order=order)
