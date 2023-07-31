# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class movie_module_class(models.Model):
    _name = 'movie.movie_module'
    _description = 'List of movies most saw'

    name_movie = fields.Char(string='Name', required=True)
    year_movie = fields.Char(string='Year of Release')
    rating_movie = fields.Integer(string='Rating of the Movie (1-5)', help="""1 = Bad
    2 = Not Bad
    3 = Meh
    4 = Good
    5 = Excellent""")
    duration = fields.Integer(string='Duration', help="Say how long the movie is")
    image = fields.Binary(string="Imagen", help="This field is for upload an image in format PNG")
    genre = fields.Selection([
        ('Opc1','Action'),
        ('Opc2','Adventures'),
        ('Opc3','Thriller'),
        ('Opc4','Animation')], string='Film Genre',required=True)
    
    @api.constrains("name_movie")
    def _validation_name_movie(self):
        for record in self:
            if self.search_count([('name_movie','=',record.name_movie)]) > 1:
                raise ValidationError(("This movie is alredy loaded! Please, register another one"))