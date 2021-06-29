from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.card import Card

cards_bp = Blueprint("cards", __name__, url_prefix="/cards")

@cards_bp.route("/<card_id>", methods=["DELETE"])
def delete_card(card_id):
    card = Card.query.get_or_404(card_id)
    db.session.delete(card)
    db.session.commit()

    return make_response(f"Card #{card.card_id} successfully deleted", 200)

@cards_bp.route("/<card_id>/like", methods=["PUT"])
def update_card(card_id):
    card = Card.query.get_or_404(card_id)
    form_data = request.get_json()
    card.likes_count = form_data["likes_count"]
    db.session.commit()
    
    return make_response(f"Card #{card.card_id} successfully updated", 200)