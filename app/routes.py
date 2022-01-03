from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.board import Board


board_bp = Blueprint('board', __name__, url_prefix="/boards")

@board_bp.route("", methods=["GET"])
def get_boards():
    all_boards = Board.query.all()
    boards_response_list = []
    for item in all_boards:
        boards_response_list.append(
            {
                "id": item.board_id,
                "title": item.title,
                "owner": item.owner
            }
        )
    return jsonify(boards_response_list)


@board_bp.route("", methods =["POST"])
def create_board():
    request_body = request.get_json()
    new_board = Board(title=request_body["title"], 
            owner=request_body["owner"])

    db.session.add(new_board)
    db.session.commit()

    return make_response(f"Board called {new_board.title} has been created", 200)


@board_bp.route("/<id>", methods=["DELETE"])
def delete_board(id):
    selected_board = Board.query.get(id)

    db.session.delete(selected_board)
    db.session.commit()

    return make_response(f"Board '{selected_board.title}' has been deleted", 200)