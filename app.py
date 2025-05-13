# app.py
from flask import Flask
from sqlalchemy.sql import text
from database import db, init_db

def create_app():
    app = Flask(__name__)
    init_db(app)

    @app.route('/')
    def index():
        return 'Hospital Management System API'

    @app.route('/test-db')
    def test_db():
        try:
            db.session.execute(text('SELECT 1'))
            return 'Database connection successful'
        except Exception as e:
            return f'Database connection failed: {str(e)}'

    from routes.doctors import doctors
    app.register_blueprint(doctors)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
