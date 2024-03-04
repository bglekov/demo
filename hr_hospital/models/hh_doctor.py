import logging

from odoo import models, fields

class Doctor(models.Model):
    _name = 'hh.doctor'
    _description = 'Doctor'

    name = fields.Char()