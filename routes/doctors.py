# routes/doctors.py
from flask import Blueprint, jsonify, request
from models.doctor import Doctor
from database import db

doctors = Blueprint('doctors', __name__)

@doctors.route('/doctors', methods=['GET'])
def get_doctors():
    doctors = Doctor.query.all()
    return jsonify([
        {
            'id': d.id,
            'name': d.name,
            'specialty': d.specialty,
            'email': d.email,
            'created_at': d.created_at,
            'appointments': []
        } for d in doctors
    ])

@doctors.route('/doctors', methods=['POST'])
def create_doctor():
    data = request.get_json()

    existing_doctor = Doctor.query.filter_by(email=data['email']).first()
    if existing_doctor:
        return jsonify({'error': 'Email already exists'}), 400

    new_doctor = Doctor(
        name=data['name'],
        specialty=data['specialty'],
        email=data['email']
    )

    db.session.add(new_doctor)
    db.session.commit()

    return jsonify({
        'id': new_doctor.id,
        'name': new_doctor.name,
        'specialty': new_doctor.specialty,
        'email': new_doctor.email,
        'created_at': new_doctor.created_at,
        'appointments': []
    }), 201
