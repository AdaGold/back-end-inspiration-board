from flask import Blueprint
from app.models.card import Card
from app.routes.route_utilities import validate_model
from ..db import db

cards_bp = Blueprint("cards_bp", __name__, url_prefix="/cards")

@cards_bp.delete("/<card_id>")
def delete_card(card_id):
    card = validate_model(Card, card_id)
    db.session.delete(card)
    db.session.commit()
    response = {"message": f"Card {card_id} deleted"}
    return response


@cards_bp.put("/<card_id>/likes")
def update_card_likes(card_id):
    card = validate_model(Card, card_id)
    card.likes_count += 1
    # print(card.likes_count)
    db.session.commit()
    return card.to_dict()