from odoo import fields, api, models, _

class EplClub(models.Model):
    _name="epl.club"

    name = fields.Char(string="Country Name")
    date_founded = fields.Date(string="Date Founded")
    home_city = fields.Char(string="Hometown")
    efl_tier = fields.Selection([('1', 'English Premier League'), ('2', 'EFL Championship'), ('3', 'EFL League One')], string="Plays In")
    players_lines = fields.One2many('epl.player', 'club_id', string="Players")