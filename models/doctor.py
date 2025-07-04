from database import db

class Doctor(db.Model):
    __tablename__ = 'doctors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    specialty = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

    appointments = db.relationship('Appointment', back_populates='doctor')
