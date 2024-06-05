# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "journal Entry Report",
    "version": "17.0.1.0.0",
    "category": "Sale",
    "sequence": 15,
    "summary": "start date to end date journal entries in XLSX report.",
    "website": "https://www.odoo.com/app/crm",
    "depends": ["sale_management", "account_accountant", "account"],
    "data": ["security/ir.model.access.csv", "wizard/jounral_entry_views.xml"],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
