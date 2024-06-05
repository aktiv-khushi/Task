# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Bulk Product",
    "version": "17.0.1.0.0",
    "category": "Sale",
    "sequence": 15,
    "summary": "Bulk Product.",
    "website": "https://www.odoo.com/app/crm",
    "depends": ["sale_management"],
    "data": [
        "security/ir.model.access.csv",
        "views/bulk_product_views.xml",
        "views/sale_order_views.xml",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
