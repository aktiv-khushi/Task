# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "So Show History",
    "version": "17.0.1.0.0",
    "category": "Sale",
    "sequence": 15,
    "summary": "Show where the product is used.",
    "website": "https://www.odoo.com/app/crm",
    "depends": ["sale_management"],
    "data": [
        "security/ir.model.access.csv",
        "views/res_config_setting_views.xml",
        "wizard/sale_order_wizard_views.xml",
        "views/sale_order_line_views.xml",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
