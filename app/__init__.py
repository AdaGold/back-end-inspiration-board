from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "SQLALCHEMY_DATABASE_URI")

    db.init_app(app)
    migrate.init_app(app, db)
    load_dotenv()

    # Import models here for Alembic setup
    from app.models.board import Board
    from app.models.card import Card

    # Register Blueprints here
    from .routes import boards_bp
    app.register_blueprint(boards_bp)

    from .routes import cards_bp
    app.register_blueprint(cards_bp)

    return app

    # CORS(app)
    # return app
