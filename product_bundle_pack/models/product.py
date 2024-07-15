from odoo import fields, models,api
from odoo.exceptions import ValidationError

class Product(models.Model):
    _inherit = 'product.template'

    is_product_pack = fields.Boolean("Is Product Pack")
    calculate_pack_price = fields.Boolean("Calculate Pack Price")
    pack_products_ids = fields.One2many('product.pack', 'product_tmpl_id',
                                        string='Pack Products')
    pack_price = fields.Integer(string="Pack Price", compute='set_pack_price',
                                store=True)

    # @api.constrains('attribute_line_ids')
    # def _check_pack_variant(self):
    #     for product in self:
    #         if product.is_product_pack and product.attribute_line_ids:
    #             raise ValidationError("You cannot create variants of the pack.")

    @api.depends('pack_products_ids', 'pack_products_ids.price')
    def set_pack_price(self):
        price = 0
        for record in self:
            for line in record.pack_products_ids:
                price = price + line.price
            record.pack_price = price

    def update_price_product(self):
        self.list_price = self.pack_price