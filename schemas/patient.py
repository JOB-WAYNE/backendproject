from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.patient import Patient

class PatientSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Patient
        include_relationships = True
        load_instance = True