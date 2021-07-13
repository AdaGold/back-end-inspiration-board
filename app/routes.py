from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.board import Board
from app.models.card import Card
from dotenv import load_dotenv
import requests
import os

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
        print('we are in the get request')
        return make_response(jsonify(boards_response), 200)
    elif request.method == "POST":
        request_body = request.get_json()
        if "title" not in request_body or "owner" not in request_body:
            return {
                "details": f"Invalid data"
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
            }
        }, 201)

# needed to delete boards to test functionality.
# We don't need to keep this production.s
@boards_bp.route("/<board_id>", methods=["DELETE"])
def handle_board(board_id):
    board = Board.query.get(board_id)
    print('board ---> ', board)

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
