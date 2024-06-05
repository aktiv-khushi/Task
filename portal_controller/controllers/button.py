from odoo import http


class OrderStateChange(http.Controller):
    @http.route(
        "/confirm_order/<int:order_id>",
        type="http",
        auth="public",
        website=True,
    )
    # confirm button click to order is confirm
    def ConfirmOrder(self, order_id, **kw):
        order = http.request.env["sale.order"].sudo().browse(order_id)
        order.state = "sale"
        return http.request.redirect("/orders")

    @http.route(
        "/cancel_order/<int:order_id>",
        type="http",
        auth="public",
        website=True,
    )
    # cancel button click to order is cancelled.
    def CancelOrder(self, order_id, **kw):
        order = http.request.env["sale.order"].sudo().browse(order_id)
        order.state = "cancel"
        return http.request.redirect("/orders")

    @http.route(
        "/duplicate_order/<int:order_id>",
        type="http",
        auth="public",
        website=True,
    )
    # duplicate button click order is duplicate.
    def duplicate_order(self, order_id, **kw):
        order = http.request.env["sale.order"].sudo().browse(order_id)
        new_order_vals = {
            "partner_id": order.partner_id.id,
            "partner_invoice_id": order.partner_invoice_id.id,
            "partner_shipping_id": order.partner_shipping_id.id,
            "order_line": [],
        }
        for line in order.order_line:
            new_order_line = {
                "name": line.name,
                "product_id": line.product_id.id,
                "product_uom_qty": line.product_uom_qty,
                "price_unit": line.price_unit,
            }
            new_order_vals["order_line"].append((0, 0, new_order_line))
        http.request.env["sale.order"].sudo().create(new_order_vals)

        return http.request.redirect("/orders")

    # @http.route('/set_draft_order/<int:order_id>',
    # type='http', auth='public', website=True)
    # def duplicate_order(self, order_id, **kw):
    #     order = http.request.env['sale.order'].sudo().browse(order_id)
    #     order.state = 'draft'
    #     return http.request.redirect('/orders')
