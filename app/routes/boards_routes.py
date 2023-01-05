from flask import Blueprint, jsonify, request
from app import db
from app.models.board import Board
from .helper_functions import get_one_obj_or_abort
import os

board_bp = Blueprint("board_bp", __name__, url_prefix="/boards")

#----------------------------------POST------------------------------
@board_bp.route("",methods=["POST"])
def add_board():
    request_body = request.get_json()

    if "title" not in request_body or "owner" not in request_body:
        return jsonify({"details": "invalid data"}), 400
    
    new_board = Board(
        title = request_body["title"],
        owner = request_body["owner"],
    )
    db.session.add(new_board)
    db.session.commit()

    return jsonify({"board": f"{new_board.title} created"}), 201

#--------------------------------GET---------------------------------