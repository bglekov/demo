import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class MyDemo(models.Model):
    _name = 'my.demo'
    _description = 'MyDemo'

    name = fields.Char()
    active = fields.Boolean(default=True, )
    date = fields.Date()
    yesterday = fields.Date()
    qty = fields.Integer()
    partnet_id = fields.Many2one(comodel_name='res.partner')
    image = fields.Image()
