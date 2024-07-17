from odoo import models, fields,api
from odoo.exceptions import ValidationError

class ProductPack(models.Model):
    _name = 'product.pack'
    _description = "Product pack"

    name = fields.Char("Name")
    product_id = fields.Many2one('product.product', string='Products',required=True,
                                 domain=[('is_product_pack', '=', False)],)
    product_tmpl_id = fields.Many2one('product.template', string='Product')
    price = fields.Float(string='Price',compute='compute_price', store=True)
    quantity = fields.Integer(string='Quantity', default=1)
    product_image = fields.Binary("Product Image", related='product_id.image_1920')

    @api.depends('product_id','quantity')
    def compute_price(self):
        for record in self:
            record.price = record.product_id.lst_price * record.quantity

    @api.constrains('quantity')
    def _check_positive_qty(self):
        for rec in self:
            if rec.quantity < 0:
                raise ValidationError("You can't enter negative quantities.")
