# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Eye Widget",
    "version": "17.0.1.0.0",
    "category": "Sale",
    "sequence": 15,
    "summary": "Track Changes to Unit Price on Purchase Orders.",
    "website": "https://www.odoo.com/app/crm",
    "depends": ['account'],
    "data": [
        'views/payment_provider_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'eye_widget/static/src/scss/eye_widget.scss',
            'eye_widget/static/src/js/eye_widget.js',
            'eye_widget/static/src/xml/eye_widget_views.xml',
        ],
    },
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}

