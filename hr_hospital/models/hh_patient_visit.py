import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class PatientVisit(models.Model):
    _name = 'hh.patient.visit'
    _description = 'PatientVisit'

    date = fields.Date()
    doctor_id = fields.Many2one(comodel_name='hh.doctor')
    patient_id = fields.Many2one(comodel_name='hh.patient')
