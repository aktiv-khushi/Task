# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "So Server Action",
    "version": "17.0.1.0.0",
    "category": "Sale",
    "sequence": 15,
    "summary": "combine customer and sale order.",
    "website": "https://www.odoo.com/app/crm",
    "depends": ["sale_management"],
    "data": [
        "security/ir.model.access.csv",
        "data/ir_action_data.xml",
        "wizard/combine_sale_order_views.xml",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
