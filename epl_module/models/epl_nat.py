from odoo import fields, api, models, _

class EplNat(models.Model):
    _name="epl.nat"

    name = fields.Char(string="Country Name")
    continent = fields.Selection([('eu', 'Europe'), ('na', 'North America'), ('sa', 'South America'), ('as', 'Asia'), ('oc', 'Oceania'), ('af', 'Africa')], string="Continent")
    players_lines = fields.One2many('epl.player', "nat_id", string="Players")