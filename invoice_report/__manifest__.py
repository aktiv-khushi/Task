# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Invoice Report",
    "version": "17.0.1.0.0",
    "category": "Sale",
    "sequence": 15,
    "summary": "Track Changes to Unit Price on Purchase Orders.",
    "website": "https://www.odoo.com/app/crm",
    "depends": ['account'],
    "data": [
        'report/action_invoice_report.xml',
        'report/invoice_report.xml',
        'report/custom_header_and_footer.xml',
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
