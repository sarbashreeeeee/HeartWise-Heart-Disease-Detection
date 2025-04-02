from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from app.config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    with app.app_context():
        # Importing model classes
        from app.models.user import User
        from app.models.metric import Metric
        from app.models.report import Report

        # Importing routes
        from app.blueprints.user_auth import routes
        from app.blueprints.main import routes
        from app.blueprints.disease_detection import routes
        from app.blueprints.dashboard import routes
        from app.blueprints.past_reports import routes

        # Register blueprints
        from app.blueprints.user_auth import user_auth_bp
        from app.blueprints.main import main_bp
        from app.blueprints.disease_detection import disease_detection_bp
        from app.blueprints.dashboard import dashboard_bp
        from app.blueprints.past_reports import past_reports_bp

        app.register_blueprint(user_auth_bp)
        app.register_blueprint(main_bp)
        app.register_blueprint(disease_detection_bp)
        app.register_blueprint(dashboard_bp)
        app.register_blueprint(past_reports_bp)

    return app
