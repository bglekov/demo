import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)

class Patient(models.Model):
    _name = 'hh.patient'
    _description = 'Patient'

    name = fields.Char()
