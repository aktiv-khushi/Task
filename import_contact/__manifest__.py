# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Import contact",
    "version": "17.0.1.0.0",
    "category": "Sale",
    "sequence": 15,
    "summary": "Track Changes to Unit Price on Purchase Orders.",
    "website": "https://www.odoo.com/app/crm",
    "depends": ["contacts"],
    "data": [
        'security/ir.model.access.csv',
        'wizard/import_contact_views.xml',
        'views/sql_query_views.xml',
        'views/order_views.xml',
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
