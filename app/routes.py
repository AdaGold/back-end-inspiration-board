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


@boards_bp.route("", methods=["GET"], strict_slashes=False)
def boards_index():
    
    boards = Board.query.all()
    boards_response = []
    
    if boards is None:
        return jsonify(boards_response), 200

    else:
        for board in boards:
            boards_response.append({
                "id": board.board_id,
                "title": board.title,
                "owner": board.owner
            })
        return jsonify(boards_response), 200

# add in relationship data that shows cards + messages etc.
@boards_bp.route("/<board_id>", methods=["GET"], strict_slashes=False)
def handle_single_board(board_id):

    board = Board.query.get(board_id)

    if board is None:
        return jsonify(f"board {board_id} doesn't exist."), 404
    
    else:
        return jsonify({"id": board.board_id,
                    "title": board.title,
                    "owner": board.owner
                }), 200


@boards_bp.route("", methods=["POST"], strict_slashes=False)
def handle_boards():
    request_body = request.get_json()

    if "title" not in request_body or "owner" not in request_body:
        return jsonify({"details": "Invalid data"}), 400
    
    new_board = Board(title= request_body["title"],
    owner= request_body["owner"])

    db.session.add(new_board)
    db.session.commit()

    return jsonify({"id": new_board.board_id}), 201


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

# change to post card to a board

# @goals_bp.route("/<goal_id>/tasks", methods=["POST"], strict_slashes=False)
# def handle_goals_tasks(goal_id):
#     request_body = request.get_json()
    
#     goal = Goal.query.get_or_404(goal_id)

#     tasks = request_body["task_ids"]

#     for task in tasks:
#         task_to_update = Task.query.get(task) 
#         task_to_update.goal_id = goal_id

#     db.session.commit()

#     return jsonify({"id": goal.goal_id,
#         "task_ids": tasks}), 200

@cards_bp.route("</board_id>/cards", methods=["POST"], strict_slashes=False)
def handle_cards(board_id):
    request_body = request.get_json()
    
    board = Board.query.get_or_404(board_id)

    if "message" not in request_body:
        return jsonify({"details": "Invalid data"}), 400

    elif len(request_body["message"]) > 40:
        return jsonify({"details": "message must be less than 40 characters."}), 400
        
    new_card = Card(message= request_body["message"])

    db.session.add(new_card)
    db.session.commit()

    return jsonify({"id": new_card.card_id,
        "message": new_card.message}), 201


@cards_bp.route("/<card_id>", methods=["DELETE"], strict_slashes=False)
def delete_single_card(card_id):
    card = Card.query.get(card_id)
    
    if card is None:
        return jsonify(f"card {card_id} doesn't exist."), 404
    
    db.session.delete(card)
    db.session.commit()

    return jsonify(f"id: {card_id} has been deleted."), 200

# @goals_bp.route("/<goal_id>/tasks", methods=["POST"], strict_slashes=False)
# def handle_goals_tasks(goal_id):
#     request_body = request.get_json()
    
#     goal = Goal.query.get_or_404(goal_id)

#     tasks = request_body["task_ids"]

#     for task in tasks:
#         task_to_update = Task.query.get(task) 
#         task_to_update.goal_id = goal_id

#     db.session.commit()

#     return jsonify({"id": goal.goal_id,
#         "task_ids": tasks}), 200