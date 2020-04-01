# Copyright 2020 Raul Carbonell
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _

class HelpDeskSetResponsable(models.TransientModel):
    _name = "helpdesk.set.responsable"

    tickets_qty = fields.Integer(
        string="Tickets Qty")

    #api model se pone pq la función default_get se ejecuta antes de que se haya creado el registro pero si que tiene acceso al model y contexto
    @api.model
    def default_get(self, fields):
        res = super(HelpDeskSetResponsable, self).default_get(fields)
        user_id = self.env.uid
        tickets=self.env['helpdesk.ticket'].search(
            [('responsable_id', '=', user_id )])
        res['tickets_qty']=len(tickets)
        return res



    def set_responsable(self):
        self.ensure_one()
        #if self._context.get('active_model') == 'helpdesk.ticket' and self._context.get('active_id', False):
        #    ticket = self.env['helpdesk.ticket'].browse(self._context.get('active_id'))
        #    ticket.responsable_id=self.env.user

        active_id=self.env.context.get('active_id')
        active_model=self.env.context.get('active_model')
        if active_id and active_model and active_model=='helpdesk.ticket':
            ticket = self.env['helpdesk.ticket'].browse(active_id)
            ticket.responsable_id=self.env.user

        return False
