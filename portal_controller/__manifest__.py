# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Portal Controller",
    "version": "17.0.1.0.0",
    "category": "Sale",
    "sequence": 15,
    "summary": "controllers",
    "website": "https://www.odoo.com/app/crm",
    "depends": ["sale_management", "website"],
    "data": ["views/template.xml", "views/order_detail_views.xml"],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
