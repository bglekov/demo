import logging
from datetime import date
from dateutil.relativedelta import relativedelta

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)


class Patient(models.Model):
    _name = 'hh.patient'
    _description = 'Patient'
    _inherit = 'hh.person.mixin'

    name = fields.Char()
    birthday = fields.Date(string="Date of birth")
    passport_series = fields.Char()
    passport_number = fields.Char()
    age = fields.Integer(compute='_compute_age')

    contact_person = fields.Many2one(
        comodel_name='hh.contact.person'
    )
    personal_doctor = fields.Many2one(
        comodel_name='hh.doctor',
        string='Favorite doctor',
    )

    diagnos_ids = fields.One2many(
        comodel_name='hh.diagnos',
        inverse_name='patient_id',
        string='Diagnoses'
    )

    @api.depends('birthday')
    def _compute_age(self):
        for rec in self:
            if rec.birthday:
                rec.age = relativedelta(
                    date.today(),
                    date(
                        rec.birthday.year,
                        rec.birthday.month,
                        rec.birthday.day
                    ),
                ).years
            else:
                rec.age = 0

    # Show patient visits by current patient
    def action_view_patient_visits(self):
        self.ensure_one()
        return {
            'name': 'Patient visits',
            'view_type': 'form',
            'view_mode': 'tree',
            'res_model': 'hh.patient.visit',
            'domain': [('patient_id', '=', self.id)],
            'type': 'ir.actions.act_window',
            'context': {'search_default_patient_id': self.id}
        }

    # Quick create patient visit
    def action_create_quick_visit(self):
        self.ensure_one()
        return {
            'name': _('New Visit'),
            'type': 'ir.actions.act_window',
            'res_model': 'hh.patient.visit',
            'view_mode': 'form',
            'context': {'default_patient_id': self.id},
            'target': 'new',
        }
