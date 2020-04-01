# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class HelpDeskTicketStage(models.Model):
    _name = "helpdesk.ticket.stage"
    _description = "Ticket Stage"

    name = fields.Char(string="name" )
