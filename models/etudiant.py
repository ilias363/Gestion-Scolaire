from odoo import fields, models, api
from datetime import date
import xlsxwriter
from io import BytesIO
import base64

class Etudiant(models.Model):
    _name = 'gestion_scolaire.etudiant'
    _description = 'Etudiant'
    
    nom = fields.Char(string='Nom')
    prenom = fields.Char(string='Prenom')
    date_naissance = fields.Date(string='Date de naissance')
    age = fields.Integer(string='Age', compute='_compute_age')
    classe_id = fields.Many2one('gestion_scolaire.classe', string='Classe')
    inscrit = fields.Boolean(string='Inscrit', default='False')
    
    @api.depends('date_naissance')
    def _compute_age(self):
        for record in self:
            if record.date_naissance:
                today = date.today()
                record.age = today.year - record.date_naissance.year - ((today.month, today.day) < (record.date_naissance.month, record.date_naissance.day))
            else:
                record.age = 0
    
    @api.onchange('classe_id')
    def _onchange_classe_id(self):
        if self.classe_id:
            self.inscrit = True
        
    def _compute_display_name(self):
        for record in self:
            record.display_name = f'{record.nom} {record.prenom}'
    
    def open_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'wizard.test',
            'view_mode': 'form',
            'target': 'new',
        }
    
    def generate_student_report_action(self):
        output = BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet("Etudiants")

        headers = ['ID Élève', "Nom de l'Élève", 'Classe', 'Age']
        for col_num, header in enumerate(headers):
            worksheet.write(0, col_num, header)

        students = self.search([])

        for row_num, student in enumerate(students, start=1):
            try: full_name = student.nom + ' ' + student.prenom
            except: full_name = ''
            worksheet.write(row_num, 0, row_num)
            worksheet.write(row_num, 1, full_name)
            worksheet.write(row_num, 2, student.classe_id.code)
            worksheet.write(row_num, 3, student.age)

        workbook.close()
        output.seek(0)
        report_data = output.getvalue()

        attachment = self.env['ir.attachment'].create({
            'name': 'students_report.xlsx',
            'type': 'binary',
            'datas': base64.b64encode(report_data),
            'store_fname': 'students_report.xlsx',
            'mimetype': 'application/vnd.ms-excel',
        })

        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{attachment.id}/?download=true',
            'target': 'self',
        }