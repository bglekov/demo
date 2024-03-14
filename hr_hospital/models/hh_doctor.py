import logging
from odoo import api, models, fields

_logger = logging.getLogger(__name__)


class Doctor(models.Model):
    _name = 'hh.doctor'
    _description = 'Doctor'
    _inherit = 'hh.person.mixin'

    name = fields.Char()
    speciality = fields.Many2one(
        comodel_name='hh.speciality',
    )
    is_intern = fields.Boolean()
    doctor_mentor = fields.Many2one(
        comodel_name='hh.doctor',
        domain="[('is_intern', '=', False),('id', '!=', id),]",
    )

    @api.onchange('is_intern', 'doctor_mentor')
    def _onchange_is_intern(self):
        if not self.is_intern:
            self.doctor_mentor = False
