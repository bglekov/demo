import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class PatientVisit(models.Model):
    _name = 'hh.patient.visit'
    _description = 'PatientVisit'

    name = fields.Char()
