from odoo import http
from odoo.http import request

class CreateTask(http.Controller):

    @http.route('/test_route', type='http', auth='public', website=True)
    def tes_create(self,  **kw):


        return request.render('lead_and_contacts_form.user_detailed_form')

