from flask import Flask
from flask_cors import CORS
import os
from .db import db, migrate
from .models.board import Board
from .routes.board_routes import boards_bp
from .routes.card_routes import cards_bp


def create_app(config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    if config:
        app.config.update(config)

    # Initialize app with SQLAlchemy db and Migrate
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints 
    app.register_blueprint(boards_bp)
    app.register_blueprint(cards_bp)

    CORS(app)
    return app
