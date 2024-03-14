import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class Illness(models.Model):
    _name = 'hh.illness'
    _description = 'Illnesses'
    _parent_name = "parent_id"

    name = fields.Char()

    parent_id = fields.Many2one('hh.illness','Parent', index=True, ondelete='cascade')
    parent_path = fields.Char(index=True)
    child_id = fields.One2many('hh.illness', 'parent_id', string='Child illnessses')

    @api.constrains('parent_id')
    def check_recursion_parent_id(self):
        if not self._check_recursion():
            raise ValueError(_('Error! You cannot create recursive categories.'))


