from odoo import http
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.http import request


class AuthSignupHomeInherit(AuthSignupHome):
    '''Handle the web signup process and redirect based on configuration.'''
    @http.route('/web/signup', type='http', auth='public', website=True, sitemap=False, csrf=False)
    def web_auth_signup(self, *args, **kw):
        response = super(AuthSignupHomeInherit, self).web_auth_signup(*args, **kw)
        option = request.env["ir.config_parameter"].sudo().get_param("controller_signup.process")
        if request.params.get('login') and option:
            return request.redirect('/welcome')
        return response


class WelcomeController(http.Controller):
    '''Render the welcome template.
    This route handles the rendering of a welcome page. It simply renders a
    specified template without needing to pass any additional context.'''

    @http.route('/welcome', type='http', auth='public', website=True, csrf=False)
    def welcome(self, **kwargs):
        return http.request.render('controller_signup.welcome_template')

    '''Render the user detail form with country and state options.

    This route handles the rendering of a user detail form, providing the necessary
    data for country and state options. It retrieves the list of all countries and states
    from the database and passes them to the template for rendering.'''

    @http.route('/user_detail', type='http', auth='public', website=True, csrf=False)
    def user_detail(self, **kwargs):
        countries = request.env['res.country'].search([])
        states = request.env['res.country.state'].search([])
        return http.request.render('controller_signup.user_detailed_form', {'countries': countries,
                                                                            'states': states})

    '''update the partner information for the current user.

    This route handles the submission of partner information via a web form.
    It updates the partner details associated with the current user based on the
    provided form data. If the form data is successfully processed, a confirmation
    message template is rendered.
'''

    @http.route('/create_partner', type='http', auth='public', website=True)
    def create_partner(self, **post):
        print(post, ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.")
        user = request.env.user
        if post:
            country_id = post.get('country')
            state_id = post.get('state')
            partner = user.partner_id
            if partner:
                partner.update({
                    'street': post.get('street1'),
                    'street2': post.get('street2'),
                    'zip': post.get('zip'),
                    'country_id': int(post.get('country')),
                    'state_id': int(post.get('state')),
                    'license': post.get('license'),
                    'language': post.get('language'),
                    'status': post.get('status'),
                    'function': post.get('job'),
                    'dob': post.get('dob'),
                    'pob': post.get('pob'),
                    'passport': post.get('passport'),
                    'mobile': post.get('no'),
                    'gender': post.get('gender'),
                    'city': post.get('city'),
                })
            return request.render("controller_signup.msg_template")

    '''Render a message template.'''

    @http.route('/msg', type='http', auth='public', website=True)
    def msg(self, **post):
        return request.render("controller_signup.msg_template")

    '''Render a message template'''

    @http.route('/success', type='http', auth="public", website=True)
    def back(self, **kw):
        return request.redirect('/web')
