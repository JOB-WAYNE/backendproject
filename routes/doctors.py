# routes/doctors.py

from flask import Blueprint, jsonify, request
from models.doctor import Doctor
from database import db

# Create a Blueprint for doctors
doctors = Blueprint('doctors', __name__, url_prefix='/doctors')

# GET /doctors - list all doctors
@doctors.route('/', methods=['GET'])
def get_doctors():
    all_doctors = Doctor.query.all()
    return jsonify([
        {
            'id': doctor.id,
            'name': doctor.name,
            'specialty': doctor.specialty,
            'email': doctor.email,
            'appointments': []  # optionally add appointments if needed
        }
        for doctor in all_doctors
    ]), 200

# POST /doctors - create a new doctor
@doctors.route('/', methods=['POST'])
def create_doctor():
    data = request.get_json()

    # Check if doctor with the same email exists
    existing_doctor = Doctor.query.filter_by(email=data.get('email')).first()
    if existing_doctor:
        return jsonify({'error': 'Email already exists'}), 400

    # Create new doctor
    new_doctor = Doctor(
        name=data.get('name'),
        specialty=data.get('specialty'),
        email=data.get('email')
    )

    db.session.add(new_doctor)
    db.session.commit()

    return jsonify({
        'id': new_doctor.id,
        'name': new_doctor.name,
        'specialty': new_doctor.specialty,
        'email': new_doctor.email,
        'appointments': []
    }), 201
