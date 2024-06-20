# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Custom Timesheet",
    "version": "17.0.1.0.0",
    "category": "Sale",
    "sequence": 15,
    "summary": "Custom timesheet",
    "website": "https://www.odoo.com/app/crm",
    "depends": ['timesheet_grid'],
    "data": [

    ],
    'external_dependencies': {
        'python': ['odoorpc']
    },
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
