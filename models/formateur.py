from odoo import models, fields, api
from datetime import date

class Formateur(models.Model):
    _name = 'gestion_scolaire.formateur'
    _description = 'Formateur'
    
    nom = fields.Char(string='Nom')
    prenom = fields.Char(string='Prenom')
    classe_ids = fields.Many2many('gestion_scolaire.classe', string='Classes')
    date_embauche = fields.Date(string="Date d'embauche")
    date_fin_service = fields.Date(string='Date de fin de service', readonly=True)
    experience = fields.Integer(string='Experience (mois)', compute='_compute_experience')
    filiere_ids = fields.Many2many('gestion_scolaire.filiere', string='Filieres')
    
    @api.depends('date_embauche')
    def _compute_experience(self):
        for record in self:
            if record.date_embauche:
                today = date.today()
                record.experience = (today.year - record.date_embauche.year) * 12 + today.month - record.date_embauche.month
            else:
                record.experience = 0
    
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.nom} {record.prenom}"