# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Show/Hide Portal Icons",
    "version": "17.0.1.0.0",
    "category": "Sale",
    "sequence": 15,
    "summary": "This module allows users to show or hide portal icons based on their preferences.",
    "website": "https://www.odoo.com/app/crm",
    "depends": ['sale_management', 'account', 'timesheet_grid','contacts'],
    "data": [
        'views/template.xml',
        'views/res_users.xml',
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
