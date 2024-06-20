# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Combine Quotations & Delete others",
    "version": "17.0.1.0.0",
    "category": "Sale",
    "sequence": 15,
    "summary": "Automatically combine duplicate quotations and delete redundant ones in sales orders.",
    "website": "https://www.odoo.com/app/crm",
    "depends": ['sale_management'],
    "data": [
        'data/ir_server_action.xml',
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
