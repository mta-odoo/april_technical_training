# -*- coding: utf-8 -*-

from odoo import http

class Gallery(http.Controller):
    
    @http.route('/gallery/', auth='user', website=True)
    def gallery(self, **kw):
        
        artworks = http.request.env['art.work'].search([('for_sale', '=', False)])
        
        return http.request.render('art_gallery.artworks_website', {
            'artworks': artworks,
        })
    

    @http.route('/gallery/<model("art.work"):artwork>', auth='user', website=True)
    def donate(self, artwork):
        user = http.request.env.user
        
        user.partner_id.artwork_ids = [(4, artwork.id, 0)]
        
        return "Thank you for donating!"