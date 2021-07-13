from flask import Blueprint, request, jsonify, make_response
from app import db
from .models.board import Board
from .models.card import Card
from dotenv import load_dotenv

# example_bp = Blueprint('example_bp', __name__)
load_dotenv()
boards_bp = Blueprint("boards", __name__, url_prefix="/boards")
cards_bp = Blueprint("cards", __name__, url_prefix="/cards")

#~~~~~~~~~~~~~~~~~~~board endpoints~~~~~~~~~~~~~~~~~~~
# Create board | Get all boards
@boards_bp.route("", methods=["POST", "GET"])
def handle_boards():
        if request.method == "GET":
            boards = Board.query.all()
            boards_response = []
            for board in boards:
                boards_response.append({
                    "id": board.board_id,
                    "title": board.title,
                    "owner": board.owner
                })
            return jsonify(boards_response, 200)

        elif request.method == "POST":
            request_body = request.get_json()

            if 'title' not in request_body or 'owner' not in request_body:
                return {"details": "Invalid data"}, 400
            new_board = Board(title=request_body["title"],
                                owner=request_body["owner"])

            db.session.add(new_board)
            db.session.commit()

            return {
                "board": {
                    "id": new_board.board_id,
                    "title": new_board.title,
                    "owner": new_board.owner
                }
            }, 201

# Get board by ID | Delete board by ID | Edit board by ID
@boards_bp.route("/<board_id>", methods=["GET", "DELETE", "PUT"])
def handle_card(board_id):
    board = Board.query.get(board_id)
    if board is None:
        return make_response("", 404)

    if request.method == "GET":
        return {
                "id": board.board_id,
                "title": board.title,
                "owner": board.owner
            }
    elif request.method == "DELETE":
        message = {"details": f"Board {board.board_id} \"{board.title}\" successfully deleted"}
        db.session.delete(board)
        db.session.commit()
        return make_response(message)
    elif request.method == "PUT":
        form_data = request.get_json()
        print("form data", form_data )

        board.title = form_data["title"]
        board.owner = form_data["owner"]

        db.session.commit()

        return make_response({
                "board": {
                    "id": board.board_id,
                    "title": board.title,
                    "owner": board.owner,
                }
        })

# Get all cards belonging to one board by ID
@boards_bp.route("/<board_id>/cards", methods=["GET"])
def get_all_cards_by_board(board_id):
    board = Board.query.get(board_id)
    if board is None:
        return make_response("", 404)

    if request.method == "GET":
        cards = Card.query.filter(Card.board_id == board_id)
        results = []
        for card in cards:
            results.append({
                "id": card.card_id,
                "message": card.message,
                "likes_count": card.likes_count,
                "board_id": card.board_id
            })

        return make_response(
                {
                    "id": board.board_id,
                    "title": board.title,
                    "tasks": results
                }, 200)

#~~~~~~~~~~~~~~~~~~~card endpoints~~~~~~~~~~~~~~~~~~~
# Create card | Get all cards
@cards_bp.route("", methods=["POST", "GET"])
def handle_cards():
        if request.method == "GET":
            cards = Card.query.all()
            cards_response = []
            for card in cards:
                cards_response.append({
                    "id": card.card_id,
                    "message": card.message,
                    "likes_count": card.likes_count,
                    "board_id": card.board_id
                })
            return jsonify(cards_response, 200)

        elif request.method == "POST":
            request_body = request.get_json()

            if 'message' not in request_body or 'likes_count' not in request_body or 'board_id' not in request_body:
                return {"details": "Invalid data"}, 400
            new_card = Card(message=request_body["message"],
                            likes_count=request_body["likes_count"],
                            board_id=request_body["board_id"])

            db.session.add(new_card)
            db.session.commit()

            return {
                "board": {
                    "id": new_card.card_id,
                    "message": new_card.message,
                    "likes_count": new_card.likes_count,
                    "board_id": new_card.board_id
                }
            }, 201

# Get card by ID | Delete card by ID | Edit card by ID
@cards_bp.route("/<card_id>", methods=["GET", "DELETE", "PUT"])
def handle_card(card_id):
    card = Card.query.get(card_id)
    if card is None:
        return make_response("", 404)

    if request.method == "GET":
        return {
                "id": card.card_id,
                "message": card.message,
                "likes_count": card.likes_count,
                "board_id": card.board_id
            }
    elif request.method == "DELETE":
        message = {"details": f"card {card.card_id} \"{card.message}\" successfully deleted"}
        db.session.delete(card)
        db.session.commit()
        return make_response(message)
    elif request.method == "PUT":
        form_data = request.get_json()
        print("form data", form_data )

        card.message = form_data["message"]
        card.likes_count = form_data["likes_count"]
        card.board_id = form_data["board_id"]

        db.session.commit()

        return make_response({
                "card": {
                    "id": card.card_id,
                    "message": card.message,
                    "likes_count": card.likes_count,
                    "board_id": card.board_id
                }
        })
