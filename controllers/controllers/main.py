from odoo import http
from odoo.http import request

'''all partner's name and image on website.'''


class Partners(http.Controller):
    """
   Route to display a list of partners.

   This method fetches all partners from the `res.partner` model and renders them
   on the website using the 'controllers.partners_detail' template.
   """

    @http.route('/partners', type='http', auth="public", website=True)
    def partners(self, **kw):
        partners = request.env['res.partner'].sudo().search([])
        return request.render('controllers.partners_detail', {
            'partners': partners
        })

    """
    Route to display information for a specific partner.
    
    This method retrieves a partner's information based on the given partner ID 
    and renders it on the website using the 'controllers.partner_info_template' template.
    """

    @http.route('/partner_information/<int:partner_id>', type='http', auth="public", website=True)
    def partner_info(self, partner_id, **post):
        partner = request.env['res.partner'].browse(partner_id)
        return request.render('controllers.partner_info_template', {'partner': partner})

    """
    Route to redirect to the partners page.
    This method redirects the user to the '/partners' URL, which displays the list of partners.
    """

    @http.route('/back', type='http', auth="public", website=True)
    def back(self, **kw):
        return request.redirect('/partners')
