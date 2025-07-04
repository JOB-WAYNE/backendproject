from marshmallow import Schema, fields, post_load
from models.appointment import Appointment

class AppointmentSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Str(required=True)
    time = fields.Str(required=True)
    doctor_id = fields.Int(required=True)
    patient_id = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)

    @post_load
    def make_appointment(self, data, **kwargs):
        return Appointment(**data)
