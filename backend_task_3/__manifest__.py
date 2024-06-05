# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Backend Task 3",
    "version": "17.0.1.0.0",
    "category": "Sale",
    "sequence": 15,
    "summary": "Track leads and close opportunities",
    "website": "https://www.odoo.com/app/crm",
    "depends": ["sale_management", "purchase"],
    "data": ["views/purchase_order_views.xml", "views/partner_views.xml"],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
