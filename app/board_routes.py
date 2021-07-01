from flask import Blueprint, json, request, jsonify, make_response
from app import db
from app.models.board import Board
from .models.card import Card

# bp route for board
board_bp = Blueprint("board", __name__, url_prefix="/board")

@board_bp.route("", methods=["GET"])
def all_boards():
    boards = Board.query.all()
    board_response = []
    for one_board in boards:
        board_response.append(one_board.get_return())
    return jsonify(board_response)

@board_bp.route("/<board_id>", methods=["GET"])
def select_board(board_id):
    board = Board.query.get(board_id)
    if board == None:
        return jsonify({"Error": "Board is not found"}, 404)
    else:
        return make_response(board.get_return(), 200)

@board_bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()

    if ("title" not in request_body or "owner" not in request_body):
        return jsonify({"details": "Failed to create a board"}), 400

    new_board = Board(title=request_body["title"], owner=request_body["owner"])
    db.session.add(new_board)
    db.session.commit()
    return jsonify({"Success": f'Board "{new_board.title}" is created'}), 201

@board_bp.route("/<board_id>", methods=["DELETE"])
def delete_one_board(board_id):
    board = Board.query.get(board_id)
    db.session.delete(board)
    db.session.commit()
    return jsonify({
        "Success": "All boards are deleted"}, 200)
# testing testing 
    # boards = Board.query.all()
    # cards = Card.query.all() ///????
    # db.session.delete(boards)
    # db.session.delete(card)
    # db.session.commit()
    # return make_response({
    #     "Success": "All boards and cards are deleted"}, 200)
