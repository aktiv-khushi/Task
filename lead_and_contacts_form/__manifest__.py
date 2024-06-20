# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Lead and contact form",
    "version": "17.0.1.0.0",
    "category": "Sale",
    "sequence": 15,
    "summary": "Track Changes to Unit Price on Purchase Orders.",
    "website": "https://www.odoo.com/app/crm",
    "depends": ['website', 'crm'],
    "data": [
        'views/template.xml',
        # 'views/create_lead.xml',
        # 'views/thank_you.xml',
        # 'views/create_contact.xml',
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
