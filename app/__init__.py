from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app(config=None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if not config:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")

    # Import models here for Alembic setup
    from app.models.board import Board
    from app.models.card import Card

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    # from .routes import example_bp
    from .routes import board_bp
    from .card_routes import card_bp
    app.register_blueprint(board_bp)
    app.register_blueprint(card_bp)

    CORS(app)
    return app
