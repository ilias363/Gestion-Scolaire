from odoo import models, fields, api

class Classe(models.Model):
    _name = 'gestion_scolaire.classe'
    _description = 'Classe'
    _rec_name = 'code'
    _sql_constraints = [
        ('code_unique', 'unique(code)', 'Le code de la classe doit être unique.')
    ]

    code = fields.Char(string='Code')
    formateur_ids = fields.Many2many('gestion_scolaire.formateur', string='Formateurs')
    etudiant_ids = fields.One2many('gestion_scolaire.etudiant', 'classe_id', string='Etudiants')
    filiere_id = fields.Many2one('gestion_scolaire.filiere', string='Filière')
    
    @api.constrains('code')
    def _check_unique_code(self):
        for record in self:
            if self.search_count([('code', '=', record.code), ('id', '!=', record.id)]) > 0:
                raise ValidationError('Le code de la classe doit être unique.')
    
