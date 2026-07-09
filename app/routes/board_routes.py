from flask import Blueprint, request, Response
from app.models.board import Board
from app.models.card import Card
from ..db import db
from .route_utilities import validate_model, create_model

boards_bp = Blueprint("boards_bp", __name__, url_prefix="/boards")

@boards_bp.get("")
def get_all_boards():
    query = db.select(Board).order_by(Board.board_id)
    boards = db.session.scalars(query)
    boards_response = []
    for board in boards:
        board_dict = board.to_dict()
        board_dict["cards_count"] = len(board.cards)
        boards_response.append(board_dict)
    return boards_response


@boards_bp.get("/<board_id>")
def get_one_board(board_id):
    board = validate_model(Board, board_id)
    boards_response = board.to_dict()
    return boards_response


@boards_bp.post("")
def make_new_board():
    request_body = request.get_json()
    return create_model(Board, request_body)


@boards_bp.post("/<board_id>/cards")
def make_new_card(board_id):
    board = validate_model(Board, board_id)
    request_body = request.get_json()
    return create_model(Card, request_body)


@boards_bp.get("/<board_id>/cards")
def get_cards_for_board(board_id):
    board = validate_model(Board, board_id)
    cards_list = []
    for card in board.cards:
        cards_list.append(card.to_dict())
    return cards_list


@boards_bp.delete("/<board_id>")
def delete_board(board_id):
    board = validate_model(Board, board_id)
    
    cards_to_delete = Card.query.filter_by(board_id=board_id).all()
    
    for card in cards_to_delete:
        db.session.delete(card)

    db.session.delete(board)
    db.session.commit()

    return Response(status=204, mimetype="application/json")