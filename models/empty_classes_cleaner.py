from odoo import models, fields, api
from datetime import date

class EmptyClassesCleaner(models.Model):
    _name = 'gestion_scolaire.cleaner'
    _description = 'delete empty classes'
    
    def delete_empty_classes(self):
        classes = self.env['gestion_scolaire.classe'].search([])
        for a_class in classes:
            student_count = self.env['gestion_scolaire.etudiant'].search_count([('classe_id', '=', a_class.id)])
            
            if student_count == 0:
                a_class.unlink()