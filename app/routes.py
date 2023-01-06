from flask import Blueprint, request, jsonify, make_response, abort
from app import db
import os
import requests
from app.models.board import Board
from app.models.card import Card

board_bp = Blueprint('boards', __name__, url_prefix="/boards")

card_bp = Blueprint('cards', __name__, url_prefix="/cards")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        if model_id:
            abort(make_response({"message": f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)
    
    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} does not exist"}, 404))

    return model 

@board_bp.route("", methods=["GET"])
def get_all_boards():

    boards = Board.query.all()
    all_boards = [board.to_dict() for board in boards]

    return jsonify(all_boards)

@board_bp.route("/<board_id>", methods=["GET"])
def get_board_by_id(board_id):

    board = validate_model(Board, board_id)

    return make_response({"boards": board.to_dict()})

def post_to_slack(message):
    url = "https://slack.com/api/chat.postMessage"

    data = {
        "channel": "C04FZS8P2BH",
        "text": message
    }
    header_key = os.environ.get("authorization")

    response = requests.post(url=url, json=data,
    headers={"Authorization": header_key})

    return response

@board_bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()

    if not "owner" in request_body or not "title" in request_body:
        abort(make_response({"status message": "Invalid data"}, 400))

    new_board = Board.create_board(request_body)

    db.session.add(new_board)
    db.session.commit()
    
    # post_to_slack(f"New board {new_board.title} has been created")

    return make_response({"boards": new_board.to_dict()}, 201)


@board_bp.route("", methods=["DELETE"])
def delete_all_boards():
    
    boards = Board.query.all()
    for board in boards:
        db.session.delete(board)
    db.session.commit()

    return make_response({"details": f"Boards successfully deleted"}, 200)


@board_bp.route("/<board_id>", methods=["DELETE"])
def delete_board_by_id(board_id):

    board = validate_model(Board, board_id)

    db.session.delete(board)
    db.session.commit()

    return make_response({"details": f'Board {board.board_id} "{board.title}" successfully deleted'}, 200)

@board_bp.route("/<board_id>/cards", methods=["POST"])
def post_card_under_board(board_id):

    board = validate_model(Board, board_id)
    request_body = request.get_json()
    card_details = request_body["message"]

    card = Card(board_id=board.board_id, likes=0, message=card_details)

    db.session.add(card)
    db.session.commit()

    response = card.to_dict()

    return make_response(response, 201)
    


