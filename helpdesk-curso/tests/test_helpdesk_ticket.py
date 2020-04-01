from odoo.tests import SavepointCase

class TestHelpDeskTicket(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.team_obj = cls.env["helpdesk.team"]
        cls.ticket_obj = cls.env["helpdesk.ticket"]

        cls.user_admin = cls.env.ref("base.user_admin")      #xml id externo del usuario


    def test_create_ticket(self):
        ticket = self.ticket_obj.create({
            "name": "Test Ticket",
            "responsable_id" : self.user_admin.id
        })

        self.assertEqual(ticket.description,"El usuario es " + self.user_admin.name)
