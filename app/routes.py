from app import db
from app.models.board import Board
from app.models.card import Card
from flask import request, Blueprint, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime
from datetime import datetime, date, time, timezone
from dotenv import load_dotenv
import os
import requests
import json

boards_bp = Blueprint("boards", __name__, url_prefix="/boards")
cards_bp = Blueprint("cards", __name__, url_prefix="/cards")


# @boards_bp.route("", methods=["GET"], strict_slashes=False)
# def boards_index():
    
#     boards = Board.query.all()
#     boards_response = []
    
#     if boards is None:
#         return jsonify(boards_response), 200

#     else:
#         for board in boards:
#             boards_response.append({
#                 "id": board.board_id,
#                 "name": board.name,
#                 "registered_at": board.register_at,
#                 "postal_code": board.postal_code,
#                 "phone": board.phone,
#                 "cards_checked_out_count": 0
#             })
#         return jsonify(boards_response), 200


# @boards_bp.route("/<board_id>", methods=["GET"], strict_slashes=False)
# def handle_single_board(board_id):

#     board = Board.query.get(board_id)

#     if board is None:
#         return jsonify(f"board {board_id} doesn't exist."), 404
    
#     else:
#         return jsonify({"id": board.board_id,
#                     "name": board.name,
#                     "registered_at": board.register_at,
#                     "postal_code": board.postal_code,
#                     "phone": board.phone,
#                     "cards_checked_out_count": 0
#                 }), 200


@boards_bp.route("", methods=["POST"], strict_slashes=False)
def handle_boards():
    request_body = request.get_json()

    if "title" not in request_body or "owner" not in request_body:
        return jsonify({"details": "Invalid data"}), 400
    
    new_board = Board(title= request_body["title"],
    owner= request_body["owner"])

    db.session.add(new_board)
    db.session.commit()

    return jsonify({"id": new_board.id}), 201


# @boards_bp.route("/<board_id>", methods=["PUT"], strict_slashes=False)
# def update_single_board(board_id):
#     board = Board.query.get(board_id)
#     request_body = request.get_json()
    
#     if board is None:
#         return jsonify(f"board {board_id} doesn't exist."), 404
    
#     elif "name" not in request_body or "postal_code" not in request_body or "phone" not in request_body:
#         return jsonify({"details": "Invalid data"}), 400

#     else:
#         board.name = request_body["name"]
#         board.postal_code = request_body["postal_code"]
#         board.phone = request_body["phone"]

#         db.session.commit()

#         return jsonify({"board": {
#             "id": board.board_id,
#             "name": board.name,
#             "registered_at": board.register_at,
#             "postal_code": board.postal_code,
#             "phone": board.phone,
#             "cards_checked_out": 0}}), 200


# @boards_bp.route("/<board_id>", methods=["DELETE"], strict_slashes=False)
# def delete_single_board(board_id):
#     board = Board.query.get(board_id)
    
#     if board is None:
#         return jsonify(f"board {board_id} doesn't exist."), 404
    
#     db.session.delete(board)
#     db.session.commit()

#     return jsonify({"id": board.board_id}), 200


# @cards_bp.route("", methods=["GET"], strict_slashes=False)
# def cards_index():
    
#     cards = Card.query.all()
#     cards_response = []
    
#     if cards is None:
#             return jsonify(cards_response), 200

#     else:
#         for card in cards:
#             cards_response.append({
#                 "id": card.card_id,
#                 "title": card.title,
#                 "release_date": card.release_date,
#                 "total_inventory": card.total_inventory,
#                 "available_inventory": 0})
#         return jsonify(cards_response), 200


# @cards_bp.route("/<card_id>", methods=["GET"], strict_slashes=False)
# def handle_single_card(card_id):

#     card = Card.query.get(card_id)
    
#     if card is None:
#         return jsonify(f"board {card_id} doesn't exist."), 404
    
#     return jsonify({
#         "id": card.card_id,
#         "title": card.title,
#         "release_date": card.release_date,
#         "total_inventory": card.total_inventory,
#         "available_inventory": 0}), 200


# @cards_bp.route("", methods=["POST"], strict_slashes=False)
# def handle_cards():
#     request_body = request.get_json()
    
#     if "title" not in request_body or "release_date" not in request_body or "total_inventory" not in request_body:
#         return jsonify({"details": "Invalid data"}), 400
    
#     new_card = Card(title= request_body["title"], 
#         release_date= request_body["release_date"],
#         total_inventory= request_body["total_inventory"])

#     db.session.add(new_card)
#     db.session.commit()

#     return jsonify({"id": new_card.card_id,
#         "title": new_card.title,
#         "release_date": new_card.release_date,
#         "total_inventory": new_card.total_inventory,
#         "available_inventory": 0}), 201


# @cards_bp.route("/<card_id>", methods=["PUT"], strict_slashes=False)
# def update_single_card(card_id):
#     card = Card.query.get(card_id)
#     request_body = request.get_json()

#     if card is None:
#         return jsonify(f"board {card_id} doesn't exist."), 404
    
#     elif "title" not in request_body or "release_date" not in request_body or "total_inventory" not in request_body:
#         return jsonify({"details": "Invalid data"}), 400

#     card.title = request_body["title"]
#     card.release_date= request_body["release_date"]
#     card.total_inventory= request_body["total_inventory"]

#     db.session.commit()

#     return jsonify({"id": card.card_id,
#         "title": card.title,
#         "release_date": card.release_date,
#         "total_inventory": card.total_inventory,
#         "available_inventory": 0}), 200


# @cards_bp.route("/<card_id>", methods=["DELETE"], strict_slashes=False)
# def delete_single_card(card_id):
#     card = Card.query.get(card_id)
    
#     if card is None:
#         return jsonify(f"board {card_id} doesn't exist."), 404
    
#     db.session.delete(card)
#     db.session.commit()

#     return jsonify({"id": card.card_id}), 200