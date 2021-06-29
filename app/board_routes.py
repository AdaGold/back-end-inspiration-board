from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.board import Board

# example_bp = Blueprint('example_bp', __name__)

# bp route for board
board_bp = Blueprint("board", __name__, url_prefix="/board")

@board_bp.route("",methods=["GET"])
def all_boards():
    boards = Board.query.all()
    board_response = []
    for one_board in boards:
        board_response.append(one_board.get_return())
    return jsonify(board_response)    