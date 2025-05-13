from flask import Blueprint, jsonify, request
from database import db
from models.appointment import Appointment
from schemas.appointment import AppointmentSchema
from marshmallow import ValidationError

appointments_bp = Blueprint('appointments', __name__, url_prefix='/appointments')

appointment_schema = AppointmentSchema()
appointments_schema = AppointmentSchema(many=True)

@appointments_bp.route('', methods=['POST'])
def create_appointment():
    try:
        data = request.get_json()
        appointment = appointment_schema.load(data, session=db.session)
        db.session.add(appointment)
        db.session.commit()
        return jsonify(appointment_schema.dump(appointment)), 201
    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@appointments_bp.route('', methods=['GET'])
def get_appointments():
    try:
        appointments = Appointment.query.all()
        return jsonify(appointments_schema.dump(appointments)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@appointments_bp.route('/<int:id>', methods=['GET'])
def get_appointment(id):
    try:
        appointment = Appointment.query.get_or_404(id)
        return jsonify(appointment_schema.dump(appointment)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

@appointments_bp.route('/<int:id>', methods=['PUT'])
def update_appointment(id):
    try:
        appointment = Appointment.query.get_or_404(id)
        data = request.get_json()
        appointment_schema.load(data, instance=appointment, session=db.session, partial=True)
        db.session.commit()
        return jsonify(appointment_schema.dump(appointment)), 200
    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@appointments_bp.route('/<int:id>', methods=['DELETE'])
def delete_appointment(id):
    try:
        appointment = Appointment.query.get_or_404(id)
        db.session.delete(appointment)
        db.session.commit()
        return jsonify({"message": "Appointment deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500