# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Age Calculate",
    "version": "17.0.1.0.0",
    "category": "Sale",
    "sequence": 15,
    "summary": "Track Changes to Unit Price on Purchase Orders.",
    "website": "https://www.odoo.com/app/crm",
    "depends": ['contacts', 'web','sale_management'],
    "data": [
        'views/res_partner_views.xml',
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
