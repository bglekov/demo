import logging
from threading import activeCount

from odoo.exceptions import UserError

from odoo import api, models, fields

_logger = logging.getLogger(__name__)


class PatientVisit(models.Model):
    _name = 'hh.patient.visit'
    _description = 'PatientVisit'
    active = fields.Boolean(default=True,compute='_compute_active')

    #name = fields.Char()
    planned_date_time = fields.Datetime(
        string='Start',
        readonly=False,
        # completed, cancelled - readonly=True
    )

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
    patient_id = fields.Many2one(comodel_name='hh.patient')
    diagnos_qty = fields.Integer(compute='_compute_diagnos_qty',store=False)


    # get a record name patient -> doctor : date
    @api.depends('doctor_id', 'patient_id', 'planned_date_time')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = "%s -> %s : %s" % (rec.patient_id.name, rec.doctor_id.name, rec.planned_date_time or '')

    @api.ondelete(at_uninstall=False)
    def _check_pissibility_for_deletion(self):
        diagnos_qty = self.env['hh.diagnos'].search_count([
            ('visit_id', '=', self._ids),
        ], limit=1)
        if diagnos_qty:
            # DON`T FORGET: from odoo.exceptions import UserError
            raise UserError(
                "Yuo can`t delete the visit. It has related diagnoses items.")

    @api.depends('diagnos_ids')
    def _compute_diagnos_qty(self):
        for rec in self:
            #if rec.diagnos_ids:
                rec.diagnos_qty = self.env['hh.diagnos'].search_count([
                    ('visit_id', '=', self._ids),
                ])
            #else:
            #    rec.diagnos_qty = 0

    @api.depends('diagnos_qty')
    def _compute_active(self):
        for rec in self:
            if rec.diagnos_qty != '0':
                rec.active = True
            else:
                rec.active = False

