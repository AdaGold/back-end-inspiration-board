from flask import Blueprint, abort, make_response, request, Response
from app.models.board import Board
from app.models.card import Card
from .route_utilities import validate_model
from ..db import db
import requests
import json
import os

bp = Blueprint("cards_bp", __name__, url_prefix="/boards/<board_id>/cards")


@bp.post("")
def create_card(board_id):

    request_body = request.get_json()

    try:
        new_card = Card.from_dict(request_body)
    except KeyError as e:
        missing_key = e.args[0]
        response = {"details": f"Invalid request body: Missing key '{missing_key}'"}
        abort(make_response(response, 400))

    if len(request_body["message"]) > 40:
        response = {
            "details": "Invalid request body: Message must be 40 characters or less"
        }
        abort(make_response(response, 400))

    db.session.add(new_card)
    db.session.commit()

    response = {"card": new_card.to_dict()}
    return response, 201


@bp.put("/<card_id>")
def agree_with_card(card_id):
    try:
        card = validate_model(Card, card_id)
    except:
        response = {"details": f"Card {card_id} not found"}
        abort(make_response(response, 404))

    card.likes_count += 1
    db.session.commit()

    response = {"card": card.to_dict()}
    return response
