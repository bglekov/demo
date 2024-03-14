import logging
from datetime import date
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models

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
