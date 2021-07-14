import re
from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.board import Board
from app.models.card import Card
from dotenv import load_dotenv
import requests

load_dotenv()
boards_bp = Blueprint("boards", __name__, url_prefix="/boards")
cards_bp = Blueprint("cards", __name__, url_prefix="/cards")

# ----------------- Board Endpoints ----------------- #
# Get all boards --> done
# Create a board --> done
@boards_bp.route("", methods=["GET", "POST"])
def handle_boards():

    if request.method == "GET":
        boards = Board.query.all()
        boards_response = []

        for board in boards:
            boards_response.append({
                "board_id": board.board_id,
                "title": board.title,
                "owner": board.owner
            })

        return make_response(jsonify(boards_response), 200)

    elif request.method == "POST":
        request_body = request.get_json()
        if "title" not in request_body:
            return {
                "details": f"Invalid data. Must include title."
            }, 400
        if "owner" not in request_body:
            return {
                "details": f"Invalid data. Must include owner."
            }, 400

        new_board = Board(
            title=request_body["title"],
            owner=request_body["owner"]
        )
        db.session.add(new_board)
        db.session.commit()

        return make_response({
            "board": {
                "id": new_board.board_id,
                "title": new_board.title,
                "owner": new_board.owner
            }
        }, 201)

# Delete a board by ID --> done
# Get a board by ID --> done
# Edit a board by ID --> done
@boards_bp.route("/<board_id>", methods=["DELETE", "GET", "PUT"])
def handle_board(board_id):
    board = Board.query.get(board_id)
    if board is None:
            return make_response(f"Board {board_id} not found. ", 404)

    if request.method == "DELETE":
        db.session.delete(board)
        db.session.commit()

        return make_response(
                {
                "details":
                    f"Board: {board.board_id} with title: {board.title}. Successfully deleted"
                }
        )

    elif request.method == "GET":
        return {
            "id": board.board_id,
            "title": board.title,
            "owner": board.owner
        }

    elif request.method == "PUT":
        form_data = request.get_json()
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


# ----------------- Card Endpoints ----------------- #
# Getting cards by board_id  --> done
# Creating a card & associating it with a specific board --> done
@boards_bp.route("/<board_id>/cards", methods=["GET", "POST"])
def handle_board_cards(board_id):

    if request.method == "POST":
        board = Board.query.get(board_id)

        if not board:
            return make_response({
                f"Board #{board_id} not found."
            }, 404)

        request_body = request.get_json()
        if "message" not in request_body:
            return {
                "details": f"Invalid, must include message."
            }

        new_card = Card(
            message=request_body["message"],
            likes_count=0,
            board_id=board.board_id
        )
        db.session.add(new_card)
        db.session.commit()

        return make_response({
            "card": {
                "id": new_card.card_id,
                "message": new_card.message,
                "likes_count": new_card.likes_count,
                "board_id": new_card.board_id
            }
        }, 201)

    elif request.method == "GET":
        board = Board.query.get(board_id)
        if not board:
            return make_response(f"Board {board_id} not found", 404)
        cards = board.cards

        list_of_cards = []

        for card in cards:
            individual_card = {
                "id": card.card_id,
                "board_id": board.board_id,
                "message": card.message,
                "likes_count": card.likes_count
            }
            list_of_cards.append(individual_card)
        return make_response({
            "id": board.board_id,
            "title": board.title,
            "owner": board.owner,
            "cards": list_of_cards
        })

# Delete a card by ID --> done
# Get card by ID --> done
# Edit card by ID --> done
@cards_bp.route("/<card_id>", methods=["DELETE", "GET", "PUT"])
def handle_card(card_id):
    card = Card.query.get(card_id)

    if card is None:
        return make_response(f"Card #{card_id} not found.", 404)

    if request.method == "DELETE":
        db.session.delete(card)
        db.session.commit()

        return make_response(
            {
                "details": f"Card at card_id: {card.card_id}. Successfully deleted"
            }
        )

    elif request.method == "GET":
        return make_response({
            "id": card.card_id,
            "message": card.message,
            "likes_count": card.likes_count,
            "board_id": card.board_id
        })

    elif request.method == "PUT":
        form_data = request.get_json()
        card.message = form_data["message"]

        db.session.commit()

        return make_response({
            "card": {
                "id": card.card_id,
                "message": card.message,
                "likes_count": card.likes_count,
                "board_id": card.board_id
            }
        })

# ----------------- Increase Card Likes ----------------- #
@cards_bp.route("/<card_id>/like", methods=["PUT"])
def handle_likes(card_id):
    card = Card.query.get(card_id)

    if card is None:
        return make_response({
            f"Card #{card_id} not found."
        }, 404)

    if request.method == "PUT":

        card.likes_count += 1
        db.session.commit()

        return make_response(
            {"likes_count": card.likes_count}
        ), 200
