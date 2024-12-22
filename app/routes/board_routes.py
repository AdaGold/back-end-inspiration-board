from flask import Blueprint, abort, make_response, request, Response
from app.models.board import Board
from ..db import db
import requests
import json
import os

bp=Blueprint("boards_bp", __name__, url_prefix="/boards")

@bp.post("")
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