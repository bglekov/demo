import logging

from odoo import models, fields

class Ilness(models.Model):
    _name = 'hh.ilness'
    _description = 'Ilness'

    name = fields.Char()