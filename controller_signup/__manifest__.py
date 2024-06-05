# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Controller Signup',
    'version': '17.0.1.0.0',
    'category': 'Sale',
    'sequence': 15,
    'summary': 'controllers',
    'website': 'https://www.odoo.com/app/crm',
    'depends': ['sale_management', 'website', 'contacts'],
    'data': [
        'views/template.xml',
        'views/user_detail_form.xml',
        'views/res_partner_views.xml',
        'views/res_config_settings_views.xml',

    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
