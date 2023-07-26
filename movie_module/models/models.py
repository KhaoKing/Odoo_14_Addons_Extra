# -*- coding: utf-8 -*-
from odoo import models, fields


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

    movie_selec = [
        ('Opc1','Action'),
        ('Opc2','Adventures'),
        ('Opc3','Thriller'),
        ('Opc4','Animation')
    ]
    genre = fields.Selection(movie_selec, string='Film Genre', required=True)



#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
