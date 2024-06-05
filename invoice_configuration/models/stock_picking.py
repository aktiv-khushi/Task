from odoo import models, fields


class StockPicking(models.Model):
    _inherit = "stock.picking"

    show_create_invoice_button = fields.Boolean(
        string="Show Create Invoice Button", compute="_compute_show_buttons"
    )
    show_create_bill_button = fields.Boolean(
        string="Show Create Bill Button", compute="_compute_show_buttons"
    )

    show_create_invoice_and_bill_button = fields.Boolean(
        string="Show Create Invoice and Bill Button",
        compute="_compute_show_buttons",
    )

    """click on create invoice button to show on invoice."""

    def action_create_invoice(self):
        invoices = self.env["account.move"]
        sale_orders = self.mapped("sale_id")
        if sale_orders:
            for order in sale_orders:
                invoice = order._create_invoices(final=True)
                invoices += invoice
        if invoices:
            action = self.env.ref(
                "account.action_move_out_invoice_type"
            ).read()[0]
            if len(invoices) > 1:
                print("\n\nif---")
                action["domain"] = [("id", "in", invoices.ids)]
            else:
                action.update(
                    {
                        "views": [
                            (self.env.ref("account.view_move_form").id, "form")
                        ],
                        "res_id": invoices.id,
                    }
                )
            return action

        return False

    """click on create bill button show on bill."""

    def action_create_bill(self):
        invoices = []
        purchase_orders = self.mapped("purchase_id")
        if purchase_orders:
            for order in purchase_orders:
                invoice = order.action_create_invoice()
                invoices.append(invoice)
        if invoices:
            bill_list = []
            for invoice in invoices:
                bill_list.append(invoice)
            action = self.env.ref(
                "account.action_move_in_invoice_type"
            ).read()[0]
            if len(bill_list) > 1:
                action["domain"] = [
                    ("id", "in", [inv["id"] for inv in bill_list])
                ]
            else:
                action["views"] = [
                    (self.env.ref("account.view_move_form").id, "form")
                ]
                action["res_id"] = bill_list[0]["res_id"]
                return action

    def action_create_invoice_bill(self):
        print("\n\ninvoice-----------")

    """button visibility on sale,purchase and sale & purchase."""

    def _compute_show_buttons(self):
        self.show_create_invoice_button = False
        self.show_create_bill_button = False
        self.show_create_invoice_and_bill_button = False
        option = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("invoice_configuration.invoice_creation_option")
        )
        for picking in self:
            if option == "sale" and picking.picking_type_id.code == "outgoing":
                picking.update(
                    {
                        "show_create_invoice_button": True,
                        "show_create_bill_button": False,
                    }
                )

            elif (
                option == "purchase"
                and picking.picking_type_id.code == "incoming"
            ):
                picking.update(
                    {
                        "show_create_bill_button": True,
                        "show_create_invoice_button": False,
                    }
                )

            elif option == "sale_purchase":
                picking.show_create_invoice_and_bill_button = True
