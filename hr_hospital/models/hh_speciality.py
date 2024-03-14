from odoo import fields, models


class Speciality(models.Model):
    _name = 'hh.speciality'
    _description = 'Speciality'

    name = fields.Char()