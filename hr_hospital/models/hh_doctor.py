import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class Doctor(models.Model):
    _name = 'hh.doctor'
    _description = 'Doctor'

    name = fields.Char()
