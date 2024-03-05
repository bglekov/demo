import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)

class Illness(models.Model):
    _name = 'hh.illness'
    _description = 'Illness'

    name = fields.Char()
