#__init__.py
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from datetime import datetime
import zoneinfo

# Initialize the extensions
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'main.login'  # Redirects to login page if unauthorized

def create_app(config_class=Config):
    # Create the Flask app instance
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize the extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    # Set the SECRET_KEY explicitly (pulling from the config or environment)
    app.config['SECRET_KEY'] = app.config.get('SECRET_KEY', 'default_secret_key')

    # Register Blueprints (routes)
    from app.routes import main
    app.register_blueprint(main)

    # Import models so they are registered with SQLAlchemy's metadata
    from app import models

    @app.template_filter('tzformat')
    def tzformat(value: datetime,
                 fmt: str = "%Y-%m-%d %H:%M",
                 tz: str = "America/Los_Angeles"):
        if not value:
            return ""
        # assume UTC if naive
        if value.tzinfo is None:
            value = value.replace(tzinfo=zoneinfo.ZoneInfo("UTC"))
        dst = value.astimezone(zoneinfo.ZoneInfo(tz))
        return dst.strftime(fmt)

    return app
