from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import request, route


class CustomerPortalInherit(CustomerPortal):

    @route(['/my/home'], type='http', auth="user", website=True)
    def home(self, **kw):
        '''This function handles the home page for the logged-in user in the customer portal.
    It toggles the visibility of the project section for the user. If the project section is currently
    hidden, it will be displayed, and vice versa'''
        res = super(CustomerPortalInherit, self).home(**kw)
        user = request.env.user
        user.project_section_hidden = not user.project_section_hidden
        return res
