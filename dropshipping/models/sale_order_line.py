from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    vendor_id = fields.Many2one('product.supplierinfo',
                                 string='Vendor',
                                 domain="[('product_tmpl_id','=',product_template_id)]")

    '''Prepare the values for a procurement.
    This method extends the base implementation to include the supplier information
    in the procurement values.'''

    def _prepare_procurement_values(self, group_id=False):
        res = super()._prepare_procurement_values(group_id)
        update = res.update({'supplierinfo_name': self.vendor_id.partner_id})
        return res
