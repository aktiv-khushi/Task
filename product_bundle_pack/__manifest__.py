# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Product Bundle Pack",
    "version": "17.0.1.0.0",
    "category": "Sale",
    "sequence": 15,
    "summary": "Track Changes to Unit Price on Purchase Orders.",
    "website": "https://www.odoo.com/app/crm",
    "depends": ['sale_management', 'stock','point_of_sale'],
    "data": [
        'security/ir.model.access.csv',
        'views/product_pack_views.xml',
        'views/product_views.xml',
        'views/sale_order_views.xml',
        'views/product_product.xml',
    ],
    "assets": {
        'point_of_sale._assets_pos': [
            'product_bundle_pack/static/src/xml/pos_product_views.xml',
            'product_bundle_pack/static/src/scss/style.scss',
            'product_bundle_pack/static/src/js/pos_product_pack.js',
        ],
    },
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
