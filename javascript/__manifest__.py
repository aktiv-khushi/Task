# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "JavaScript",
    "version": "17.0.1.0.0",
    "category": "Sale",
    "sequence": 15,
    "summary": "Track Changes to Unit Price on Purchase Orders.",
    "website": "https://www.odoo.com/app/crm",
    "depends": ['website', 'web', 'crm'],
    "data": [
        # 'views/assets.xml',
        'views/template.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'javascript/static/src/js/modify_webpage.js',
        ],
    },
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
