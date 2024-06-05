# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Invoice Configuration",
    "version": "17.0.1.0.0",
    "category": "Sale",
    "sequence": 15,
    "summary": "Craete invoice from picking",
    "website": "https://www.odoo.com/app/crm",
    "depends": ["base", "stock", "sale", "purchase", "account"],
    "data": [
        "views/res_config_settings_views.xml",
        "views/stock_picking_views.xml",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
