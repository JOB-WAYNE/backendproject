from flask import Flask
from flask_cors import CORS
from sqlalchemy.sql import text
from flask_migrate import Migrate
from database import db, init_db

def create_app():
    app = Flask(__name__)
    init_db(app)

    CORS(app)

    migrate = Migrate(app, db)

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

    # ✅ Import and register blueprints
    from routes.doctors import doctors
    from routes.appointments import appointments_bp

    app.register_blueprint(doctors)
    app.register_blueprint(appointments_bp)

    return app

# ✅ Add this to run the app if this file is executed directly
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
