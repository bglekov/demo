from odoo import api, models, fields


class Diagnos(models.Model):
    _name = 'hh.diagnos'
    _description = 'Diagnos'

    visit_id = fields.Many2one(comodel_name='hh.patient.visit',string="Visit",required=True)
    illness_id = fields.Many2one(comodel_name='hh.illness')
    appointment = fields.Char(string="Appointment for treatment")
    approved = fields.Boolean()

    #view reference fields
    doctor_id = fields.Many2one(
        comodel_name='hh.doctor',
        related='visit_id.doctor_id',
        readonly=True
    )

    patient_id = fields.Many2one(
        comodel_name='hh.patient',
        related='visit_id.patient_id',
        readonly=True
    )

