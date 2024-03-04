import logging

from odoo import models, fields

class Patient(models.Model):
    _name = 'hh.patient'
    _description = 'Patient'

    name = fields.Char()