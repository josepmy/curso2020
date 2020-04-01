from odoo import api, fields, models, _

class ProjectTaskTicket(models.Model):
    _inherit = "project.task"

    ticket_ids = fields.One2many(
        string="Tickets",
        comodel_name="helpdesk.ticket",
        inverse_name="task_id",
    )



    tickets_count = fields.Integer(
        compute='_compute_tickets_count',
        string="Number of Tickets"
    )

    tickets_open_count = fields.Integer(
        compute='_compute_tickets_count',
        string="Number of Open Tickets"
    )



    def _compute_tickets_count(self):
        for task in self:
            task.tickets_count=len(task.ticket_ids)
            task.tickets_open_count=len(task.ticket_ids.search(
            [('stage_id.id','!=','4'),('task_id','=',task.id)]
            ))


    def action_new_ticket(self):
        action = self.env.ref("helpdesk_project.task_action_ticket_new").read()[0]
        action['context']={
            "default_task_id" : self.id,
            "default_project_id" : self.project_id and self.project_id.id,
        }
        return action

    def action_view_tickets_open(self):
        action = self.env.ref('helpdesk_project.task_action_ticket_tree_open').read()[0]
        action['context'] = {
            'search_task_id': self.id,
        }
        return action
