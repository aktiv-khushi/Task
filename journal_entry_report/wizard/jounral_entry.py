import base64
from io import BytesIO

import xlsxwriter
from odoo import fields, models
from odoo.exceptions import UserError


class JournalReportWizard(models.TransientModel):
    _name = "journal.report.wizard"
    _description = "Journal Report Wizard"

    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    company_ids = fields.Many2many(
        res_model="res.company", string="Companies", required=True
    )

    """A journal entry occurs between the start date
    and end date in XLSX report."""

    def action_print_report(self):
        domain = [
            ("date", ">=", self.start_date),
            ("date", "<=", self.end_date),
            ("company_id", "in", self.company_ids.ids),
        ]
        journal_entries = self.env["account.move"].search(domain)

        if not journal_entries:
            raise UserError(
                "No journal entries found for the specified date range and companies."
            )

        output = BytesIO()
        workbook = xlsxwriter.Workbook(output, {"in_memory": True})
        sheet = workbook.add_worksheet("Journal Entries")
        bold = workbook.add_format({"bold": True})
        row = 0

        """The enumerate() function adds a counter as
        the key of the enumerate object."""

        headers = [
            "Date",
            "Journal",
            "Entry Number",
            "Reference",
            "Company",
            "Amount",
        ]
        for col_num, header in enumerate(headers):
            sheet.write(0, col_num, header, bold)

        row = 1
        for entry in journal_entries:
            sheet.write(row, 0, str(entry.date))
            sheet.write(row, 1, entry.journal_id.name)
            sheet.write(row, 2, entry.name)
            sheet.write(row, 3, entry.ref or "")
            sheet.write(row, 4, entry.company_id.name)
            sheet.write(row, 5, entry.amount_total)
            row += 1

        workbook.close()
        output.seek(0)
        file_data = output.read()

        attachment = self.env["ir.attachment"].create(
            {
                "name": f"Journal_Entries_{self.start_date}_to_{self.end_date}.xlsx",
                "type": "binary",
                "datas": base64.b64encode(file_data),
            }
        )

        return {
            "type": "ir.actions.act_url",
            "url": f"/web/content/{attachment.id}?download=true",
            "target": "self",
        }
