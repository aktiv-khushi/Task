# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Vendor's dropshipping",
    "version": "17.0.1.0.0",
    "category": "Sale",
    "sequence": 15,
    "summary": "vendor for dropshipping.",
    "website": "https://www.odoo.com/app/crm",
    "depends": ['sale_management', 'stock', 'purchase'],
    "data": [
        'views/sale_order_line_views.xml',
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
