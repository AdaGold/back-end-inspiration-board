from flask import Blueprint, json, request, jsonify, make_response
from app import db
from app.models.board import Board

# bp route for board
board_bp = Blueprint("board", __name__, url_prefix="/board")

@board_bp.route("", methods=["GET"])
def all_boards():
    boards = Board.query.all()
    board_response = []
    for one_board in boards:
        board_response.append(one_board.get_return())
    return jsonify(board_response)

@board_bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()

    if ("title" not in request_body or "owner" not in request_body):
        return jsonify({"details": "Failed to create a board"}), 400

    new_board = Board(title=request_body["title"], owner=request_body["owner"])
    db.session.add(new_board)
    db.session.commit()
    return jsonify({"Success": f'Board "{new_board.title}" is created'}), 201

@board_bp.route("", methods=["DELETE"])
def delete_all_boards():
    boards = Board.query.all()
    db.session.delete(boards)
    db.session.commit()
    return make_response({
        "Success": "All boards are deleted"}, 200)

    # boards = Board.query.all()
    # cards = Card.query.all() ///????
    # db.session.delete(boards)
    # db.session.delete(card)
    # db.session.commit()
    # return make_response({
    #     "Success": "All boards and cards are deleted"}, 200)