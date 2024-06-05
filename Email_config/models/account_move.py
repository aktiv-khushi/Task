from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = "account.move"

    email_sent = fields.Boolean(default=False)

    """ Invoice date is equal to today or less than today.
        Automatically trigger email to the customer of the invoice.
        Once the email is sent to the customer"""

    @api.model
    def _send_invoice_emails(self):
        invoices = self.search(
            [
                ("invoice_date_due", "<=", fields.Date.today()),
                ("email_sent", "=", False),
                ("state", "=", "posted"),
            ]
        )
        for invoice in invoices:
            if invoice.partner_id.email:
                body = (f"Hello {invoice.partner_id.name},"
                        f"<br/>This is to remind you that your invoice "
                        f"#{invoice.name} is due on "
                        f"{invoice.invoice_date_due}.")
                self.env["mail.mail"].create(
                    {
                        "subject": "Invoice Due Reminder",
                        "body_html": body,
                        "email_to": invoice.partner_id.email,
                    }
                ).send()
                invoice.email_sent = True
                # SEND_MAIL()
