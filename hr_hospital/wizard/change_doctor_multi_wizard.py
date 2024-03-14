import logging
from odoo import fields, models

_logger = logging.getLogger(__name__)


class PatientChangeDoctorMulti(models.TransientModel):
    _name = 'hh.patient.change.doctor.multi.wizard'
    _description = 'Wizard for mass change doctor in patients'

    new_doctor_id = fields.Many2one(
        comodel_name='hh.doctor',
        string='New Doctor'
    )

    def action_write_doctor(self):
        active_ids = self.env.context.get('active_ids')
        patient_ids = self.env['hh.patient'].browse(active_ids)
        for patient in patient_ids:
            patient.personal_doctor = self.new_doctor_id.id
