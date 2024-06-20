from datetime import timedelta, datetime

from odoo import models, api, fields
from odoo.exceptions import ValidationError


class AnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    @api.model
    def create(self, vals):
        '''Overrides the create method to add validation checks for the date field.
        This method ensures that the date of the timesheet entry is not more than 7 days in the past
        and is not on a Saturday or Sunday. It calls the _check_date method for this validation.'''
        self._check_date(vals['date'])
        return super(AnalyticLine, self).create(vals)

    def write(self, vals):
        '''Overrides the write method to add validation checks for the date field and restrict editing
        to users in the 'Timesheet Manager' group or administrators.'''

        if not (self.env.user.has_group('hr_timesheet.group_timesheet_manager')):
            raise ValidationError("Only managers or administrators can edit timesheet entries.")
        if 'date' in vals:
            self._check_date(vals['date'])
        return super(AnalyticLine, self).write(vals)

    def _check_date(self, date_str):
        date_entry = fields.Date.from_string(date_str)
        current_datetime = datetime.now()
        seven_days_ago = current_datetime - timedelta(days=7)

        # Check if the date is more than 7 days in the past
        if date_entry < seven_days_ago.date():
            # Get the last Monday at 4 PM from the current date
            last_monday = current_datetime - timedelta(days=current_datetime.weekday())
            last_monday_4pm = last_monday.replace(hour=16, minute=0, second=0)

            if current_datetime > last_monday_4pm:
                raise ValidationError("Timesheet Entry is locked for this Date.")

        # Check if the date is a Saturday or Sunday
        if date_entry.weekday() in (5, 6):
            raise ValidationError("Cannot fill Saturday and Sunday timesheets.")
