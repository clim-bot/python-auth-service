from flask_migrate import Migrate
from .models import db

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)  # Initialize Flask-Migrate

    app.register_blueprint(auth_blueprint)

    return app
