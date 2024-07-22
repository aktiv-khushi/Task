# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "My Custom Widget",
    "version": "17.0.1.0.0",
    "category": "Sale",
    "sequence": 15,
    "summary": "Track Changes to Unit Price on Purchase Orders.",
    "website": "https://www.odoo.com/app/crm",
    "depends": ["web"],
    "data": [
        'views/new_component.xml',
        'views/res_partner.xml',
        'views/assest.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'custom_widget/static/src/component/new/*'
            'custom_widget/static/src/js/color_picker_widget.js',
        ],
    },
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
