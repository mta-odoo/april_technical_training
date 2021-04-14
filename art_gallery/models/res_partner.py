# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    artwork_ids = fields.Many2many(string='Art Works', comodel_name='art.work')
    
    is_donor = fields.Boolean(compute="_compute_donor")
    
    @api.depends('artwork_ids')
    def _compute_donor(self):
        for r in self:
            r.is_donor = True if r.artwork_ids else False