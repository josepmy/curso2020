# Copyright 2020 Raul Carbonell
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _

class ResUsersTicket(models.Model):
    _inherit = "res.users"

    helpdesk_code = fields.Char(string="HelpDesk Code")

    ticket_ids = fields.Many2many(
        string="Field name",
        comodel_name="helpdesk.ticket",
        relation="helpdesk_ticket_users_rel",
        column1="user_id",
        column2="helpdesk_ticket_id",
    )

    team_id = fields.Many2one(
        string="Team",
        comodel_name="helpdesk.team",
    )


    team_id = fields.Many2one(
        string="Team",
        comodel_name="helpdesk.team",
    )
