from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_product_pack = fields.Boolean("Is Product Pack")
    calculate_pack_price = fields.Boolean("Calculate Pack Price")
    pack_products_ids = fields.One2many('product.pack', 'product_tmpl_id',
                                        string='Pack Products', copy=True)
    pack_price = fields.Integer(string="Pack Price", compute='set_pack_price',
                                store=True)

    # pack_price = fields.Integer(string="Pack Price", compute='set_pack_price',
    #                             store=True,
    #                             help='The calculated price of the pack.')
    # pack_products_ids = fields.One2many('pack.products', 'product_tmpl_id',
    #                                     string='Pack Products', copy=True,
    #                                     help='The list of products included '
    #                                          'in the pack.')
    pack_quantity = fields.Integer(string='Pack Quantity')

    # pack_location_id = fields.Many2one('stock.location',
    #                                    domain=[('usage', 'in',
    #                                             ['internal', 'transit'])],
    #                                    default=default_pack_location,
    #                                    string='Pack Location',
    #                                    help='The default location for the pack.')

    @api.depends('pack_products_ids', 'pack_products_ids.price')
    def set_pack_price(self):
        price = 0
        for record in self:
            for line in record.pack_products_ids:
                price = price + line.price
            record.pack_price = price

    def update_price_product(self):
        self.list_price = self.pack_price

    @staticmethod
    def _pos_fields():
        print("\n\n\n\n2222222222222222222")
        fields = super(ProductTemplate, ProductTemplate)._pos_fields()
        fields.append('is_product_pack')
        return fields


class ProductProduct(models.Model):
    _inherit = 'product.product'

    is_product_pack = fields.Boolean(string='Is Product Pack')

    @staticmethod
    def _pos_fields():
        print("\n\n\n\n33333333333333333333333333")
        fields = super(ProductProduct, ProductProduct)._pos_fields()
        fields.append('is_product_pack')
        return fields
