# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class ArtWorkTheme(models.Model):
    _name = 'art.work.theme'
    _description = 'Art Work Theme'

    name = fields.Char(string='Name')
    main_color = fields.Selection(string='Color',
                             selection=[('red', 'Red'),
                                        ('blue', 'Blue'),
                                        ('green', 'Green')])
    
    artwork_id = fields.Many2one('art.work')
    
    
class ArtWork(models.Model):
    _name = 'art.work'
    _description = 'Art Work'

    name = fields.Char(string='Name')
    
    author_id = fields.Many2one(string='Author', comodel_name='res.partner', ondelete='cascade')
    
    donations_ids = fields.Many2many(string='Donations', comodel_name='res.partner', ondelete='cascade')
    
    theme_ids = fields.One2many(string='Themes', comodel_name='art.work.theme', inverse_name='artwork_id')

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