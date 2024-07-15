# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Multiple Images POS",
    "version": "17.0.1.0.0",
    "category": "Sale",
    "sequence": 15,
    "summary": "Track Changes to Unit Price on Purchase Orders.",
    "website": "https://www.odoo.com/app/crm",
    "depends": ["point_of_sale"],
    "data": [
        'views/pos_setting_views.xml',
        'views/product_pos_views.xml',
    ],
    "assets": {
        'point_of_sale._assets_pos': [
            'multiple_img_pos/static/src/js/image_popup.js',
            'multiple_img_pos/static/src/js/icon.js',
            'multiple_img_pos/static/src/xml/icon.xml',
            'multiple_img_pos/static/src/scss/style.scss',
            'multiple_img_pos/static/src/xml/image_popup.xml',
        ],
    },
        "installable": True,
        "application": True,
        "license": "LGPL-3",
    }

