from odoo import fields, api, models, _

class EplPlayer(models.Model):
    _name = "epl.player"

    name = fields.Char(string="Player Name")
    age = fields.Integer(string="Age")
    club_id = fields.Many2one('epl.club', string="Club")
    nat_id = fields.Many2one('epl.nat', string="Nationality")
    play_position = fields.Selection([('cf', 'Center Forward'), ('lw', 'Left Winger'), ('rw', 'Right Winger'), ('lm', 'Left Midfield'), ('cm', 'Center Midfield'), ('rm', 'Right midfield'), ('fb', 'Full Back'), ('cb', 'Center Back'), ('gk', 'Goalkeeper')])
    goals_scored = fields.Integer(string="Goals Scored")
    apps_made = fields.Integer(string="Appearances Made")
    # club_ids = fields.Many2many('epl.club', string="Has Played For:") relTable D.N.E.


