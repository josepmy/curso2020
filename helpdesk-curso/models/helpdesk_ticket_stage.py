# Copyright 2020 Raul Carbonell
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _


class HelpDeskTicketStage(models.Model):
    _name = "helpdesk.ticket.stage"
    _description = "Ticket Stage"

    name = fields.Char(string="name" )
