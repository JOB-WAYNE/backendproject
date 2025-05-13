from marshmallow import Schema, fields, validates, ValidationError

class DoctorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    specialty = fields.Str(required=True)
    email = fields.Email(required=True)
    created_at = fields.DateTime(dump_only=True)
    appointments = fields.List(fields.Nested('AppointmentSchema'), dump_only=True)

    @validates('email')
    def validate_email(self, value):
        if not value:
            raise ValidationError("Email cannot be empty")

doctor_schema = DoctorSchema()
