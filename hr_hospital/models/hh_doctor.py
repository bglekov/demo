import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class Doctor(models.Model):
    _name = 'hh.doctor'
    _description = 'Doctor'
    _inherit = 'hh.person.mixin'

    name = fields.Char()
    speciality = fields.Many2one(
        comodel_name='hh.speciality',
        required=True,
    )
