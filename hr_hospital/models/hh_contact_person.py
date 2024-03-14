from odoo import api, fields, models


class Contact_Person(models.Model):
    _name = 'hh.contact.person'
    _description = 'Contact persons'
    _inherit = 'hh.person.mixin'

    name = fields.Char(compute='_compute_name', store=True)

    # def write(self, vals):
    #     self.name = "%s %s" % (self.first_name, self.last_name or '')

    @api.depends('first_name', 'last_name')
    def _compute_name(self):
        for rec in self:
            rec.name = "%s %s" % (rec.first_name, rec.last_name or '')

    # @api.model
    # def create(self, vals_list):
    #     self.name = "%s %s" % (self.first_name, self.last_name or '')
