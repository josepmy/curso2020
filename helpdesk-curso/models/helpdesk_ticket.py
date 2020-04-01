# Copyright 2020 Josep M Yepes
# License AGPL-3.0 or later

from odoo import api, fields, models, _

class HelpdeskTicket(models.Model):

	_name = 'helpdesk.ticket'

	name = fields.Char(string='Name', required=True)
	description = fields.Text(string='Description')
	date_deadline = fields.Datetime(string='Date limit')

