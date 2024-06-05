from odoo import http
from odoo.http import request


class Orders(http.Controller):
    @http.route("/orders", type="http", auth="public", website=True)
    # if user is availabe so his order is show
    #  else this is public user so sign in first.

    def orders_page(self, **kwargs):
        user = request.env.user
        if user and user.id and not user._is_public():
            orders = request.env["sale.order"].search(
                [("partner_id", "=", user.partner_id.id)]
            )
            return http.request.render(
                "portal_controller.orders_page_template", {"orders": orders}
            )
        else:
            return http.request.render(
                "portal_controller.signin_prompt_template"
            )

    @http.route(
        "/orders_information/<int:order_id>",
        type="http",
        auth="public",
        website=True,
    )
    # if user are available so his information is show.
    def order_details_page(self, order_id, **kw):
        orders = http.request.env["sale.order"].browse(order_id)
        return http.request.render(
            "portal_controller.order_info_template", {"sale_order": orders}
        )
