from flask import Blueprint, jsonify, request
from models.patient import Patient
from database import db  # <-- FIXED

patients = Blueprint('patients', __name__)

@patients.route('/patients', methods=['GET'])
def get_patients():
    patients = Patient.query.all()
    return jsonify([
        {
            'id': p.id,
            'name': p.name,
            'date_of_birth': p.date_of_birth,
            'email': p.email,
            'created_at': p.created_at
        } for p in patients
    ])

@patients.route('/patients', methods=['POST'])
def create_patient():
    data = request.get_json()
    new_patient = Patient(
        name=data['name'],
        date_of_birth=data['date_of_birth'],
        email=data['email']
    )
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({
        'id': new_patient.id,
        'name': new_patient.name,
        'date_of_birth': new_patient.date_of_birth,
        'email': new_patient.email,
        'created_at': new_patient.created_at
    }), 201
