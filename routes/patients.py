from flask import Blueprint, request, jsonify
from models.patient import Patient
from database import db

patients_bp = Blueprint('patients', __name__, url_prefix='/patients')

# Create a new patient
@patients_bp.route('/', methods=['POST'])
def create_patient():
    data = request.get_json()
    new_patient = Patient(
        name=data.get('name'),
        age=data.get('age'),
        email=data.get('email')
    )
    db.session.add(new_patient)
    db.session.commit()

    return jsonify({
        'id': new_patient.id,
        'name': new_patient.name,
        'age': new_patient.age,
        'email': new_patient.email
    }), 201

# Get all patients
@patients_bp.route('/', methods=['GET'])
def get_patients():
    patients = Patient.query.all()
    return jsonify([
        {
            'id': p.id,
            'name': p.name,
            'age': p.age,
            'email': p.email
        } for p in patients
    ])
