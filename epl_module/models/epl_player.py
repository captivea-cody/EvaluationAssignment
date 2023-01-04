from odoo import fields, api, models, _
from odoo.exceptions import UserError

class EplPlayer(models.Model):
    _name = "epl.player"
  
    name = fields.Char(string="Player Name")
    age = fields.Integer(string="Age")
    club_id = fields.Many2one('epl.club', string="Club")
    transfer_id = fields.Many2one('epl.club', string="Transferring To:")
    nat_id = fields.Many2one('epl.nat', string="Nationality")
    play_position = fields.Selection([('cf', 'Center Forward'), ('lw', 'Left Winger'), ('rw', 'Right Winger'), ('lm', 'Left Midfield'), ('cm', 'Center Midfield'), ('rm', 'Right midfield'), ('fb', 'Full Back'), ('cb', 'Center Back'), ('gk', 'Goalkeeper')])
    goals_scored = fields.Integer(string="Goals Scored")
    apps_made = fields.Integer(string="Appearances Made")
    club_ids = fields.Many2many('epl.club', string="Has Played For:")

    def action_make_transfer(self):
        if self.transfer_id.id == False:
            raise UserError("Please set a transfer destination for this player.")
        elif self.transfer_id == self.club_id:
            raise UserError("Transfer target can't be player's current club.")
        else:
            if self.transfer_id not in self.club_ids:
                self.write({'club_ids':[(4,self.transfer_id.id)]})
            self.club_id = self.transfer_id.id


