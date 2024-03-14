from odoo import api, models, fields


class PersonMixin(models.AbstractModel):
    _name = 'hh.person.mixin'
    _description = "Persons"

    first_name = fields.Char()
    last_name = fields.Char()
    phone = fields.Char()
    email = fields.Char()
    photo = fields.Image()
    sex = fields.Selection(
        selection=[
            ('male', 'Male'),
            ('female', 'Female'),
        ]
    )


