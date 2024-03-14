from odoo import fields, models
from datetime import date
from dateutil.relativedelta import relativedelta


class DiagnosesMonthListWizard(models.TransientModel):
    _name = 'hh.diagnos.month.list'
    _description = 'Diagnoses per month'

    doctor_ids = fields.Many2many(comodel_name='hh.doctor')
    illness_ids = fields.Many2many(comodel_name='hh.illness', string='Illnesses')
    start_date = fields.Date(default=date.today().replace(day=1))
    end_date = fields.Date(default=date.today() + relativedelta(day=31))

    diagnos_ids = fields.Many2many(comodel_name='hh.diagnos',string='Diagnoses')


    def action_show_diagnoses(self):
        #generate domain for filter
        domain=[]
        if self.doctor_ids:
            domain += [('doctor_id', 'in', self.doctor_ids.ids)]
        if self.illness_ids:
            domain += [('illness_id', 'in', self.illness_ids.ids)]
        if self.start_date and self.end_date:
            domain += [('create_date', ">=", self.start_date), (('create_date', "<=", self.end_date))]

        diagnos_ids = self.env['hh.diagnos'].search(domain)

        return {
            'name': 'Invoice Report Wizard',  # The name of the action, should be the same as the wizard
            'type': 'ir.actions.act_window',
            'res_model': 'invoice.report.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': self.env.context,
        }

    def action_open_wizard(self):
        return {
            'name': _('Create diagnos list Wizard'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hh.diagnos.month.list',
            'target': 'new',
            'context': self.env.context,
        }
