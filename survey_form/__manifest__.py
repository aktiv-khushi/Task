# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Survey form",
    "version": "17.0.1.0.0",
    "category": "Sale",
    "sequence": 15,
    "summary": "Track Changes to Unit Price on Purchase Orders.",
    "website": "https://www.odoo.com/app/crm",
    "depends": ['website', 'website_sale', "web", 'base'],
    "data": [
        'views/template.xml',
        'views/res_partner_views.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'survey_form/static/src/css/survey_form_radio.css',
            # 'survey_form/static/src/js/salary_range.js',
        ],
    },
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
