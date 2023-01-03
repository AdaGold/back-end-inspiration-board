from flask import Blueprint, request, jsonify, make_response, abort
from flask_sqlalchemy import SQLAlchemy
from app import db
from app.models.board import Board

board_bp = Blueprint('boards', __name__, url_prefix="/boards")

card_bp = Blueprint('cards', __name__, url_prefix="/cards")

# def validate_model(model_id):

@board_bp.route("/boards", methods=["GET"])
def get_all_boards():
    pass

@board_bp.route("/boards/<board_id>", methods=["GET"])
def get_board_by_id(board_id):
    pass

@board_bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()

    if not "owner" in request_body or not "description" in request_body:
        abort(make_response({"status message": "Invalid data"}, 400))

    new_board = Board(owner=request_body["owner"],title=request_body["title"])

    db.session.add(new_board)
    db.session.commit()

@board_bp.route("/boards/<board_id>/cards", methods=["GET"])
def get_all_cards(board_id):
    pass


@card_bp.route("/cards/<card_id>", methods=["POST"])
def create_new_card(card_id):
    pass

@card_bp.route("/cards", methods=["GET"])
def get_all_cards():
    pass

@card_bp.route("/<boards_id>/card/<card_id>", methods=["PATCH"])
def update_likes_in_card(board_id, card_id):
    pass



