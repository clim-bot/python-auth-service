from flask import Flask  # Ensure Flask is imported
from .routes import auth_blueprint
from .config import Config
from .models import db  # Import the database instance

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(auth_blueprint)

    return app
