# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Sale Commission",
    "version": "17.0.1.0.0",
    "category": "Sale",
    "sequence": 15,
    "summary": "Manage sales commissions for partners and sales orders.",
    "website": "https://www.odoo.com/app/crm",
    "depends": ['sale_management', 'contacts'],
    "data": [
        'views/sale_oder_views.xml',
        'views/sale_order_line_views.xml',
        'views/res_partner.xml',
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
