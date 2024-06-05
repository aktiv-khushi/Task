# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Email Configuration",
    "version": "17.0.1.0.0",
    "category": "Sale",
    "sequence": 15,
    "summary": "Email Configuration state wise change email template.",
    "website": "https://www.odoo.com/app/crm",
    "depends": ["sale_management"],
    "data": ["views/sale_order_views.xml", "data/ir_cron.xml"],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
