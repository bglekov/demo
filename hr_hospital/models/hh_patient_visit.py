import logging

from odoo import models, fields


class PatientVisit(models.Model):
    _name = 'hh.patient.visit'
    _description = 'PatientVisit'

    name = fields.Char()