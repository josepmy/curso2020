# Copyright 2020 Raul Carbonell
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _


class HelpdeskTicket(models.Model):

    _name = 'helpdesk.ticket'
<<<<<<< HEAD
    _description = 'Ticket'

    #haciendo esta herencia, se mete el chater en el modelo
    #También se tiene que meter en las dependencias
    #También se tiene que meter el div oe_chatter en el  view
    _inherit = ['mail.thread.cc', 'mail.activity.mixin']


    name = fields.Char(string='Name', required=True)
    description = fields.Text('Description')
    date_deadline = fields.Datetime('Date limit',tracking=True) #Tracking si tenemos chatter, nos hace seguimiento de las modificaciones
    team_id = fields.Many2one(
        string="Team",
        comodel_name="helpdesk.team",
    )

    responsable_id = fields.Many2one(
        string="Responsable",
        comodel_name="res.users",
    )

    user_ids = fields.Many2many(
        string="Users",
        comodel_name="res.users",
        relation="helpdesk_ticket_users_rel",
        column1="helpdesk_ticket_id",
        column2="user_id",
        domain="[('team_id', '=', team_id)]",
    )

    tickets_qty = fields.Integer(
        string="Tickets Qty",
        compute='_compute_tickets_qty',
        store=True,
    )

    @api.depends("responsable_id" )
    def _compute_tickets_qty(self):
        ticket_obj=self.env['helpdesk.ticket']
        for ticket in self:
            tickets=ticket_obj.search(
                [('responsable_id', '=', ticket.responsable_id.id )])
            ticket.tickets_qty=len(tickets)



    def action_equipo1(self):
        return self.write({'team_id': 1})

    def set_responsable(self):
        self.ensure_one()                   #Sólo se ejecuta para un registro (Desde el formulario)
        self.responsable_id=self.env.user   #obtener usuario actual (objeto user se mete en el campo de tipo user)
        # self.write({
        #    'responsable_id': self.env.user.id
        #})
        #HAce lo mismo que arriba, pero es mejor usar este caso comentado, cuando tengamos que actualizar mas de un registro


    #AL modificarl el campo name o el campo date_deadline, en la descripción se pondrá el name + date_deadline
    @api.onchange("name", "date_deadline", )
    def _onchange_description(self):
        if self.name and self.date_deadline:
            self.description='%s - %s'%(self.name, self.date_deadline)
            #self.description=self.name + self.date_deadline


    @api.model
    def create(self, vals):
        responsable = vals.get('responsable_id','1')  #si no hay valor le asiga un 1
        user=self.env['res.users'].browse(responsable)
        vals.update({'description': 'El usuario es ' + user.name})

        res = super(HelpdeskTicket, self).create(vals)

        return res
=======

    name = fields.Char(string='Name', required=True)
    description = fields.Text('Description')
    date_deadline = fields.Datetime('Date limit')
>>>>>>> 56292683f3156f90b3516e33e709425c48075bf1
