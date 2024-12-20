from flask import Blueprint, request
from ..db import db
from app.models.board import Board

boards_bp=Blueprint("boards_bp", __name__, url_prefix="/boards")

@boards_bp.get("")
def get_all_boards():
  query = db.select(Board).order_by(Board.board_id)
  boards = db.session.scalars(query)

  boards_response = [board.to_dict() for board in boards]
  return boards_response

