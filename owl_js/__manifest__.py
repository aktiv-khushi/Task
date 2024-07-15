# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Owl JS",
    "version": "17.0.1.0.0",
    "category": "Sale",
    "sequence": 15,
    "summary": "Track Changes to Unit Price on Purchase Orders.",
    "website": "https://www.odoo.com/app/crm",
    "depends": ['website_sale'],
    "data": [
        'views/template.xml',
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
    'assets': {
        'web.assets_frontend': [
            # 'owl_js/static/src/js/public_widget.js',
            'owl_js/static/src/js/include_public_widget.js',
        ]
    }
}
