from odoo import models
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    """Get the context and recognize the button."""

    def action_view_sales_orders(self):
        email_type = self.env.context.get("email_type")
        self._send_mail(email_type)

    """If there is a State Quotation then the Quotation Information
    will look like Mail and if there is a State sale Order then
    the Order Information will look like Mail and if partner no
    have email so ValidationError came and saw."""

    def _send_mail(self, email_type):
        for order in self:
            if not order.partner_id.email:
                raise ValidationError(
                    "The customer does not have an email address."
                )
            if email_type == "quotation":
                if order.order_line and order.state == "draft":
                    subject = "Quotation Information"
                    body = (
                        f"Hello {order.partner_id.name},"
                        f"<br/>This is to let you know that "
                        f"your quotation is {order.amount_total} amount."
                    )
                elif order.state == "sale":
                    subject = "Empty quotation"
                    body = (
                        f"Hello {order.partner_id.name},"
                        f"<br/>This is to let you know that "
                        f"your quotation is empty."
                    )
                else:
                    subject = "Empty quotation"
                    body = (
                        f"Hello {order.partner_id.name},"
                        f"<br/>This is to let you know that "
                        f"your quotation is empty."
                    )
                mail_values = {
                    "subject": subject,
                    "body_html": body,
                    "email_to": order.partner_id.email,
                }
                self.env["mail.mail"].create(mail_values).send()

            elif email_type == "sale_order":
                if order.order_line and order.state == "sale":
                    subject = "Sale Order Information"
                    body = (
                        f"Hello {order.partner_id.name},"
                        f"<br/>This is to let you know that "
                        f"your sale order is {order.amount_total} amount."
                    )
                elif order.state == "draft":
                    subject = "Empty sale order"
                    body = (
                        f"Hello {order.partner_id.name},"
                        f"<br/>This is to let you know that your "
                        f"sale order is empty."
                    )
                else:
                    subject = "Empty sale order"
                    body = (f"Hello {order.partner_id.name},"
                            f"<br/>This is to let you know that "
                            f"your sale order is empty.")
                mail_values = {
                    "subject": subject,
                    "body_html": body,
                    "email_to": order.partner_id.email,
                }
                self.env["mail.mail"].create(mail_values).send()
