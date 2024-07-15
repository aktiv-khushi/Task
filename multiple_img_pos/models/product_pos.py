from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    attachment_ids = fields.Many2many('ir.attachment', 'class_ir_attachments_rel', 'class_id', 'attachment_id', 'Attachments')
