from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Filiere(models.Model):
    _name = 'gestion_scolaire.filiere'
    _description = 'Filiere'
    _rec_name = 'nom'
    _sql_constraints = [
        ('code_unique', 'unique(code)', 'Le code de la filière doit être unique.')
    ]

    nom = fields.Char(string='Nom')
    code = fields.Char(string='Code')
    classe_ids = fields.One2many('gestion_scolaire.classe', 'filiere_id', string='Classes')
    formateur_ids = fields.Many2many('gestion_scolaire.formateur', string='Formateurs')

    @api.constrains('code')
    def _check_unique_code(self):
        for record in self:
            if self.search_count([('code', '=', record.code), ('id', '!=', record.id)]) > 0:
                raise ValidationError('Le code de la filière doit être unique.')