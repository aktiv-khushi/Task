from odoo import models, fields


class ProductPack(models.Model):
    _name = 'product.pack'
    _description = "Product pack"

    name = fields.Char("Name")
    product_tmpl_id = fields.Many2one('product.template', string='Product')
    price = fields.Float(string='Price')
    quantity = fields.Integer(string='Quantity', default=1)
    product_image = fields.Binary("Product Image", related='product_tmpl_id.image_1920')
