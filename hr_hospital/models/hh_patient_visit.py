import logging
from odoo.exceptions import UserError
from odoo import api, models, fields

_logger = logging.getLogger(__name__)


class PatientVisit(models.Model):
    _name = 'hh.patient.visit'
    _description = 'PatientVisit'
    active = fields.Boolean(default=True, store=True)

    #name = fields.Char()
    planned_date_time = fields.Datetime(
        string='Start',
        readonly=False,
        # completed, cancelled - readonly=True
    )
    planned_date = fields.Date(index=True)

    fact_date_time = fields.Datetime(
        string='Date-time fact',
        readonly=False,
        # completed, cancelled - readonly=True
    )

    doctor_id = fields.Many2one(
        comodel_name='hh.doctor',
        readonly=False,
        # completed, cancelled - readonly=True
        required=True,
        index=True,
    )

    visit_status = fields.Selection(
        selection=[
            ('planned', 'Planned'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled'),
        ],
        string='Status',
        required=True,
        default='planned',
        change_default=True,
    )

    diagnos_ids = fields.One2many(comodel_name='hh.diagnos',inverse_name='visit_id',string='Diagnoses')
    patient_id = fields.Many2one(comodel_name='hh.patient', index=True)
    diagnos_qty = fields.Integer(compute='_compute_diagnos_qty',store=False)


    # get a record name patient -> doctor : date
    @api.depends('doctor_id', 'patient_id', 'planned_date_time')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = "%s -> %s : %s" % (rec.patient_id.name, rec.doctor_id.name, rec.planned_date_time or '')


    @api.depends('diagnos_ids')
    def _compute_diagnos_qty(self):
        for rec in self:
            rec.diagnos_qty = len(rec.diagnos_ids)


    @api.depends('planned_date_time')
    def _onchange_planned_date_time(self):
        for rec in self:
            if rec.planned_date_time:
                rec.planned_date = rec.planned_date_time.date()


    @api.constrains('active')
    def _check_active_value(self):
        for rec in self:
            if not rec.active and rec.diagnos_qty > 0:
                raise UserError("Patient visit has some diagnoses. You cannot archive it.")


    @api.constrains('planned_date_time','doctor_id','patient_id')
    def _check_uniq_doctor_patient_date(self):
        for rec in self:
            if self.search_count(
                [
                    ('patient_id', '=', rec.patient_id.id),
                    ('doctor_id', '=', rec.doctor_id.id),
                    ('planned_date', '=', rec.planned_date)
                ]
            ) > 1:
                raise UserError("You cannot create visit for same doctor and patient on same day")


    @api.ondelete(at_uninstall=False)
    def _check_pissibility_for_deletion(self):
        # diagnos_qty = self.env['hh.diagnos'].search_count([
        #     ('visit_id', '=', self._ids),
        # ], limit=1)
        if self.diagnos_qty:
            # DON`T FORGET: from odoo.exceptions import UserError
            raise UserError(
                "You can`t delete the visit. It has related diagnoses items.")