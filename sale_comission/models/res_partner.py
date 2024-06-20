from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    sale_commission_count = fields.Integer('Sale commission count', compute='_compute_sale_commission_count')

    '''Computes the sales Commission count for each partner and stores the result in the `sale_commission_count` field.'''

    def _compute_sale_commission_count(self):
        for partner in self:
            partner.sale_commission_count = self.env['sale.order.line'].search_count(
                [('order_id.partner_id', '=', partner.id)])

    '''Returns an action for viewing the sales commission history related to the current partner.'''

    def action_view_sales_commission(self):
        return {
            'name': 'Sales Commission History',
            'domain': [('order_id.partner_id', '=', self.id)],
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'sale.order.line',
            'type': 'ir.actions.act_window',
        }
