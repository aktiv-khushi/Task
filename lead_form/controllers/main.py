from odoo import http
from odoo.http import request


class CreateTask(http.Controller):

    @http.route('/route_lead', type='http', auth='public', website=True)
    def tes_create(self, **kw):
        print('\n\nBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBb\n\n', kw)
        contact = kw.get('contact')
        print('contact---111111-', contact)
        return request.render('lead_form.lead_and_contact_form')

    @http.route('/success', type='http', auth='public', website=True)
    def success(self, **kw):
        print('success---->', kw)

        return request.render('lead_form.thank_you')
