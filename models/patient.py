from datetime import datetime
from database import db  # Import db from database.py

class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    appointments = db.relationship('Appointment', backref='patient', lazy=True)

    def __repr__(self):
        return f"<Patient {self.name}>"