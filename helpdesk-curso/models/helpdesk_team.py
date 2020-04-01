# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class HelpDeskTeam(models.Model):
    _name = "helpdesk.team"
    _description = "HelpDesk Team"

    name = fields.Char(string="name" )
    ticket_ids = fields.One2many(
        string="Tickets",
        comodel_name="helpdesk.ticket",
        inverse_name="team_id",
    )

    user_ids = fields.One2many(
        string="Users",
        comodel_name="res.users",
        inverse_name="team_id",
    )
