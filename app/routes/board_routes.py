from flask import Blueprint, abort, make_response, request, Response
from app.models.board import Board
from app.models.card import Card
from ..db import db
import requests
import json
import os
from .route_utilities import validate_model

boards_bp = Blueprint("boards_bp", __name__, url_prefix="/boards")


@boards_bp.post("")
def create_board():
    request_body = request.get_json()

   
    try:
        new_board = Board.from_dict(request_body)
    except KeyError as e:
        missing_key = e.args[0]
        response = {"details": f"Invalid request body: Missing key '{missing_key}'"}
        abort(make_response(response, 400))
    


    db.session.add(new_board)
    db.session.commit()

    response = {"board": new_board.to_dict()}
    return response, 201


@boards_bp.get("")
def get_all_boards():
    try:
        query = db.select(Board).order_by(Board.id)
        boards = db.session.scalars(query).all()

        boards_response = [board.to_dict() for board in boards]
        return boards_response, 200
    except Exception as e:
        print(f"Error fetching boards: {e}")  
        return {"error": "An error occurred while fetching boards."}, 500
        
@boards_bp.get("/<board_id>")
def get_single_board(board_id):
    board = validate_model(Board, board_id)

    return board.to_dict()

@boards_bp.put("/<board_id>")
def update_board(board_id):
    board = validate_model(Board, board_id)
    request_body = request.get_json()

    board.title = request_body["title"]
    board.owner = request_body["owner"]

    db.session.commit()

    return Response( f'Task {board_id} "{board.title}" successfully updated' )

@boards_bp.delete("/<board_id>")
def delete_board(board_id):
    board = validate_model(Board,board_id)

    db.session.delete(board)
    db.session.commit()

    return Response(f'Task {board_id} "{board.title}" successfully deleted' )