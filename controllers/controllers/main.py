from odoo import http
from odoo.http import request


'''all partner's name and image on website.'''


class Partners(http.Controller):

    @http.route('/partners', type='http', auth="public", website=True)
    def partners(self, **kw):
        partners = request.env['res.partner'].sudo().search([])
        return request.render('controllers.partners_detail', {
            'partners': partners
        })

    @http.route('/partner_information/<int:partner_id>', type='http', auth="public", website=True)
    def partner_info(self, partner_id, **post):
        partner = request.env['res.partner'].browse(partner_id)
        return request.render('controllers.partner_info_template', {'partner': partner})

    @http.route('/back', type='http', auth="public", website=True)
    def back(self, **kw):
        return request.redirect('/partners')



