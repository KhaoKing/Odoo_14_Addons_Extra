# -*- coding: utf-8 -*-

from odoo import models, fields


class movie_module_class(models.Model):
    _name = 'movie.movie_module'
    _description = 'List of movies most saw'

    name_movie = fields.Char(string='Movie Name', required=True)
    year_movie = fields.Integer(string='Movie Year')
    rating_of_the_movie = fields.Float (string='Raiting of the Movie', compute="_value_pc", store=True)
    duration = fields.Float(string='Duration')
    genere = fields.Text(string='Genere')







#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
