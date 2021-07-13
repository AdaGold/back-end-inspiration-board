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

# Deleting a single board instance
@boards_bp.route("/<board_id>", methods=["DELETE"])
def handle_board(board_id):
    board = Board.query.get(board_id)

    if request.method == "DELETE":
        if board is None:
            return make_response(f"Board {board_id} not found. ", 404)

        db.session.delete(board)
        db.session.commit()

        return make_response(
                {
                "details":
                    f"Board: {board.board_id} with title: {board.title}. Successfully deleted"
                }
        )

# Getting board and associated cards or creating cards and associating a board
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