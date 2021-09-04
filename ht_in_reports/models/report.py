from odoo import api,fields, models,_
from datetime import date, datetime
from odoo.exceptions import UserError, ValidationError
from dateutil.relativedelta import relativedelta


class AccountMove(models.Model):
    _inherit = "account.move"
    _description = "Journal Entry"
    _order = 'date desc, name desc, id desc'
    _mail_post_access = 'read'
    _check_company_auto = True
    _sequence_index = "journal_id"

    due_balance = fields.Float(string='Due Balance')
    gst_number = fields.Char(string='GSTIN')
