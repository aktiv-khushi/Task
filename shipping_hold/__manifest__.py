# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Shipping Hold",
    "version": "17.0.1.0.0",
    "category": "Sale",
    "sequence": 15,
    "summary": "sale order and delivery customization",
    "website": "https://www.odoo.com/app/crm",
    "depends": ["sale_management", "stock"],
    "data": ["views/sale_order_views.xml", "views/stock_picking_views.xml"],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
