from odoo import http
from odoo.http import request

class MyWebServiceController(http.Controller):

    @http.route('/ws/get_classe', type='http', auth='public', methods=['GET'], csrf=False)
    def get_classe(self):
        class_id = request.httprequest.args.get('class_id')
        
        if not class_id:
            return "error: class_id is null"

        try:
            class_id = int(class_id)
        except ValueError:
            return "error: Invalid ID format"
        
        class_record = request.env['gestion_scolaire.classe'].sudo().search([('id', '=', class_id)], limit=1)
        if not class_record:
            return "error: Class not found."
        
        return f'''{dict(
            code=class_record.code,
            filiere=class_record.filiere_id.nom,
            formateurs=[formateur.nom+' '+formateur.prenom for formateur in class_record.formateur_ids],
            etudiants=[etudiant.nom+' '+etudiant.prenom for etudiant in class_record.etudiant_ids]
            )}'''
        
    @http.route('/ws/create_etudiant', type='json', auth='public', methods=['POST'], csrf=False)
    def create_etudiant(self):
        data = request.httprequest.get_json()
        nom = data.get('nom')
        prenom = data.get('prenom')
        date_naissance = data.get('date_naissance')
        classe_id = data.get('classe_id')
        
        if not nom or not prenom or not date_naissance or not classe_id:
            return {"error": "Not enough required fields."}
        
        new_record = request.env['gestion_scolaire.etudiant'].sudo().create({
            'nom' : nom,
            'prenom' : prenom,
            'date_naissance' : date_naissance,
            'classe_id' : classe_id
        })
        return {"id_etudiant": new_record.id}