from odoo import api, fields, models, _

class HelpDeskTicketProject(models.Model):
    _inherit = "helpdesk.ticket"

    project_id = fields.Many2one(
        'project.project',
        string='Project')

    task_id = fields.Many2one(
        'project.task',
        string='Task')

    @api.onchange("task_id" )
    def _onchange_task_id(self):
        if self.task_id and self.task_id.project_id:
            self.project_id = self.task_id.project_id
        else:
            self.project_id = False


    @api.onchange("project_id" )
    def _onchange_project_id(self):
        vals = {
            'domain' : {
                'task_id':[('project_id','=',self.project_id.id)]
            }
        }
        return vals
