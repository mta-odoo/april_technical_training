# -*- coding: utf-8 -*-

from odoo import models, fields, api


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