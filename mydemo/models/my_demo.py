import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)

class MyDemo(models.Model):
    _name = 'my.demo'
    _description = 'MyDemo'

    name = fields.Char()

    active = fields.Boolean(default=True, )