from flask import Blueprint, request, jsonify, make_response, abort
from app import db
import os
import requests
from app.models.board import Board

board_bp = Blueprint('boards', __name__, url_prefix="/boards")

# card_bp = Blueprint('cards', __name__, url_prefix="/cards")

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

    new_board = Board(owner=request_body["owner"],title=request_body["title"])

    db.session.add(new_board)
    db.session.commit()
    
    post_to_slack(f"New board {new_board.title} has been created")

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

@board_bp.route("/<board_id>/cards", methods=["GET"])
def get_all_cards(board_id):

    board = validate_model(Board, board_id)

    get_cards = Board.query.get(board)

    return make_response({"boards": get_cards.to_dict()})

# @board_bp.route("/<board_id>/cards", methods=["GET"])
# def get_all_cards(board_id):
#     pass

    board = validate_model(Board, board_id)

    cards_list = []

    for card in board.cards: 
        card_dict = card.to_dict()
        card_dict["board_id"] = card.board_id
        cards_list.append(card_dict)

    return_body = {
        "board_id": board.board_id,
        "owner": board.owner,
        "title": board.title,
        "cards": cards_list
    }

    return jsonify(return_body), 200




