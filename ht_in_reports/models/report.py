from odoo import api,fields, models,_
from datetime import date, datetime
from odoo.exceptions import UserError, ValidationError
from dateutil.relativedelta import relativedelta


# class SaleOrder(models.Model):

#     _inherit = 'sale.order'
    
#     due_date = fields.Char(string='Due Date')

class PdfReports(models.Model):

    _name = 'in.report'
    _description = 'PDF Invoices'
    _inherit = 'mail.thread'

    name = fields.Many2one('res.partner', string="Company Name", track=True)
    street1 = fields.Char(string="Address Line")
    street2 = fields.Char(string="Address line 2")
    city = fields.Char(string='City')
    pin_code = fields.Integer(string='Pin code', track=True)
    state = fields.Many2one('res.country.state', string='State')
    country = fields.Many2one('res.country', string='Country')
    # address = fields.Text(string="Address", related='name.')
    inv_date = fields.Date(string='Invoice Date')
    due_date = fields.Date(string='Due Date', track=True)
    sub_total = fields.Float(string='Sub Total')
    total = fields.Float(string='Total')
    payment_made = fields.Float(string='Payment Made')
    balance_due = fields.Float(string='Balance Due')
    gst_no = fields.Char(string="GSTIN")
    inv_num = fields.Char(string='Invoice Number',default=lambda self:_('New'), copy=False, tracking=True, track=True)
    pro_line_ids = fields.One2many('sale.order.line', 'rep_id' ,string="Product Lines")
    company = fields.Many2one('res.company', string='Company Name')

    @api.model
    def create(self,vals):
        
        if vals.get('inv_num',_('New')) == _('New'):
            vals['inv_num'] = self.env['ir.sequence'].next_by_code('in.report') or _('New')
        
        res = super(PdfReports,self).create(vals)
        return res

    class SaleOrderLine(models.Model):

        _inherit = 'sale.order.line'

        rep_id = fields.Many2one('in.report', string='Report Lines')