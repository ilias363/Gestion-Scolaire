from odoo import models, fields, api

class WizardTest(models.TransientModel):
    _name = 'wizard.test'
    _description = 'Wizard'

    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')

    def button_do_something(self):
        # Implement your action here, for example, create a new record in another model
        self.env['another.model'].create({
            'name': f"{self.first_name} {self.last_name}",
            # other fields
        })
        return {'type': 'ir.actions.act_window_close'}

