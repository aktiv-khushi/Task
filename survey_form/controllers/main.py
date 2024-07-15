from odoo import http
from odoo.http import request


class SurveyForm(http.Controller):

    @http.route('/survey_form', type='http', auth='public', website=True)
    def survey_form(self, **kw):
        print('survey form----------->')
        return request.render('survey_form.details_template')

    @http.route('/success', type='http', auth='public', website=True)
    def success(self, **kw):
        print('survey form-------tur---->')
        return request.render('survey_form.thank_you')
