# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PartnerWizard(models.TransientModel):
    _name = 'gallery.partner.wizard'
    _description = 'Wizard: Add donations for Art Work'
    
    def _default_artwork(self):
        return self.env['art.work'].browse(self._context.get('active_id'))
    
    artwork_id = fields.Many2one(comodel_name='art.work', string='Art Work', default=_default_artwork)
    
    donors = fields.Many2many('res.partner')
    
    def set_donors(self):
        for donor in self.donors:
            donor.artwork_ids = [(4, self.artwork_id.id, 0)]
        