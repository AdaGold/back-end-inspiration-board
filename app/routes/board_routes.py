from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.board import Board
from app.models.card import Card


board_bp = Blueprint('board', __name__, url_prefix="/boards")


#Helper function
def valid_int(number):
    try:
        return int(number)     
    except:
        abort(make_response({"error": f"{number} must be an int"}, 400))
#Helper function
def get_board_from_id(board_id):
    board_id = valid_int(board_id)
    board = Board.query.get(board_id)
    if board:
        return board
    else:
        abort(make_response({"description": "Board not found"}, 404))

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
    

    return make_response({"board_id": new_board.board_id}, 200)


@board_bp.route("/<id>", methods=["DELETE"])
def delete_board(id):
    selected_board = Board.query.get(id)

    db.session.delete(selected_board)
    db.session.commit()

    return make_response(f"Board '{selected_board.title}' has been deleted", 200)


# POST /board/1/card
# POST { title: "sbsdgsd" } to localhost:5000/board/1/card
# POST { title: "title 2" } to localhost:5000/board/1/card3

@board_bp.route("/<id>/card", methods=["POST"])
def post_cards_of_board (id):
    request_body = request.get_json()
    # board = get_board_from_id(id)
    if "message" not in request_body:
        return make_response({"details":"Invalid data"}, 400)
    new_card = Card(
        message=request_body["message"],
        likes_count=0,
        # board_id=request_body["id"]
        board_id=id
    )

    # board.cards.append(new_card)

    db.session.add(new_card)
    
    db.session.commit()

    return make_response(jsonify({"board_id":new_card.board_id, "message":new_card.message}))
    # return make_response(jsonify({"board_id":id, "board_cards":board.cards}))

@board_bp.route("/<board_id>/cards", methods=["GET"])  # get cards belong to one board
def get_cards_of_one_board(board_id):
    board = get_board_from_id(board_id)
    board_cards = [card.to_dict() for card in board.cards]
    return jsonify({
                   "id": board.board_id,
                   "title" : board.title,
                   "cards": board_cards
    })
    return make_response(jsonify({
                   board_cards
    }))