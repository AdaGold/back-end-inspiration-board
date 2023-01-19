from flask import Blueprint, jsonify, request
from app import db
from app.models.board import Board
from app.models.card import Card
from .helper_functions import get_one_obj_or_abort
import os

board_bp = Blueprint("board_bp", __name__, url_prefix="/boards")

#----------------------------------POST------------------------------
@board_bp.route("",methods=["POST"])
def add_board():
    request_body = request.get_json()

    if "title" not in request_body or "owner" not in request_body:
        return jsonify({"details": "invalid data"}), 400
    
    new_board = Board(
        title = request_body["title"],
        owner = request_body["owner"],
    )
    db.session.add(new_board)
    db.session.commit()

    return jsonify({"board": f"{new_board.title} created"}), 201

#--------------------------------GET---------------------------------
@board_bp.route("", methods=["GET"])
def get_all_boards():

    boards = Board.query.all()

    response = [board.create_board_dict() for board in boards]

    return jsonify(response), 200

@board_bp.route("/<board_id>", methods=["GET"])
def get_one_board(board_id):
    board = get_one_obj_or_abort(Board, board_id)

    return jsonify({"board": board.create_board_dict()}), 200

#------------------------GET CARDS-------------------------------

@board_bp.route("/<board_id>/cards", methods=["GET"])
def get_cards_from_board(board_id):
    board = get_one_obj_or_abort(Board, board_id)

    response = [card.create_dict() for card in board.cards]

    board_dict = {
        "board_id": board.board_id,
        "title": board.title,
        "owner": board.owner,
        "cards": response
    }

    return jsonify(board_dict), 200

#------------------------POST CARDS--------------------------------

@board_bp.route("/<board_id>/cards", methods=["POST"])
def post_card_to_board(board_id):
    board = get_one_obj_or_abort(Board, board_id)

    request_body = request.get_json()

    for card_id in request_body["card_ids"]:
        card = get_one_obj_or_abort(Card, card_id)

        card.board_id = board_id

        db.session.add(card)
        db.session.commit()
    
    return jsonify({"Card with card id": request_body["card_ids"], "Linked to board id": board.board_id}), 200

#---------------------DELETE-------------------------------

@board_bp.route("/<board_id>", methods=["DELETE"])
def delete_one_board(board_id):
    board = get_one_obj_or_abort(Board, board_id)

    db.session.delete(board)
    db.session.commit()

    return jsonify({"details": f"Board id: {board_id} was deleted"}), 200
