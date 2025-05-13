from marshmallow import Schema, fields

class AppointmentSchema(Schema):
    id = fields.Int(dump_only=True)
    doctor_id = fields.Int(required=True)
    patient_id = fields.Int(required=True)
    appointment_date = fields.DateTime(required=True)
    created_at = fields.DateTime(dump_only=True)

appointment_schema = AppointmentSchema()
