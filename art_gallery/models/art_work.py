# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class ArtWork(models.Model):
    _name = 'art.work'
    _description = 'Art Work'

    name = fields.Char(string='Name')

    length = fields.Float(string='Length')
    width = fields.Float(string='Width')
    
    frame = fields.Selection(string='Frame',
                             selection=[('gold', 'Gold'),
                                        ('black', 'Black'),
                                        ('none', 'None')])
    
    
    finished_date = fields.Date(string='Finished Date')
    
    active = fields.Boolean(default=True)
    
    owner_name = fields.Char()
    
    for_sale = fields.Boolean()
    
    public_message = fields.Char()
    
    
    @api.onchange('owner_name', 'for_sale')
    def _onchange_public_message(self):
        self.ensure_one()        
        if self.for_sale:
            self.public_message = "This art work is on sale."
        else:
            self.public_message = "The owner is %s" % self.owner_name

            
    @api.constrains('finished_date')
    def _check_date(self):
        for r in self:
            if r.finished_date > fields.Date.today():
                raise ValidationError("Finished date cannot be higher than today: %s" % r.finished_date)