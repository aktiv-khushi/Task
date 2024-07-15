from odoo import models, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def get_description(self, product_id=False):
        product =  self.browse(int(product_id))
        return product.display_name or product.description_sale