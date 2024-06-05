from odoo import models, fields


# from odoo.exceptions import ValidationError


class BulkProduct(models.Model):
    _name = "bulk.product"
    _description = "Bulk Product"

    name = fields.Char(string="Name", required=True)
    master_product = fields.Many2one(
        "product.template", string="Master Product", required=True
    )
    bulk_products = fields.One2many(
        "bulk.product.line", "bulk_product_id", string="Bulk Products"
    )
    user_id = fields.Many2one("res.partner", string="User", required=True)
    email = fields.Char(string="Email", required=True)


class BulkProductLine(models.Model):
    _name = "bulk.product.line"
    _description = "Bulk Product Line"

    bulk_product_id = fields.Many2one(
        "bulk.product", string="Bulk Product", required=True
    )
    product_id = fields.Many2one(
        "product.product",
        string="Product",
        required=True,
        domain=[("detailed_type", "=", "product")],
    )

    """either domain or validation"""
    """If the product is not storable then put a validation"""

    # @api.onchange('product_id')
    # def _onchange_product_id(self):
    #     if self.product_id and self.product_id.detailed_type != 'product':
    #         raise ValidationError("You can only select storable product.")
