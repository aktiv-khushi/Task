# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Product Bundle Pack",
    "version": "17.0.1.0.0",
    "category": "Sale",
    "sequence": 15,
    "summary": "Track Changes to Unit Price on Purchase Orders.",
    "website": "https://www.odoo.com/app/crm",
    "depends": ['sale_management','product'],
    "data": [
        'security/ir.model.access.csv',
        'views/product_pack_views.xml',
        'views/product_views.xml',
        'views/sale_order_views.xml',
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
