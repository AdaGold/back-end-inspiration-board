from flask import Blueprint, request, jsonify, make_response, abort
from flask_sqlalchemy import SQLAlchemy
from app import db
from app.models.board import Board
from app.models.card import Card
from app.routes import validate_model

card_bp = Blueprint('cards', __name__, url_prefix="/cards")

@card_bp.route("", methods=["POST"])
def create_new_card():
    request_body = request.get_json()

    if "likes" not in request_body or "message" not in request_body:
        return make_response(jsonify({"details":"Invalid data"}), 400)
    
    new_card = Card.from_dict(request_body)

    db.session.add(new_card)
    db.session.commit()

    return make_response(jsonify({"card":new_card.to_dict()}), 201)

@card_bp.route("", methods=["GET"])
def get_all_cards():
    cards_response = []
    cards = Card.query.all()

    cards_response = [card.to_dict() for card in cards]
    print(cards_response)

    return jsonify(cards_response), 200

@card_bp.route("/<card_id>", methods=["GET"])
def get_one_card(card_id):
    card = validate_model(Card, card_id)
    return make_response(jsonify({"card":card.to_dict()}), 200)


@card_bp.route("/<card_id>", methods=["DELETE"])
def delete_card(card_id):
    card = validate_model(Card, card_id)

    db.session.delete(card)
    db.session.commit()

    return make_response({"details": f"Card {card_id} \"{card.message}\" successfully deleted"}), 200
    

@card_bp.route("/<card_id>", methods=["PATCH"])
def update_likes_in_card(card_id):
    card = validate_model(Card, card_id)

    request_body = request.get_json()

    card.likes = request_body['likes'] + 1

    db.session.commit()

    return make_response(jsonify({"card":card.to_dict()}), 200)

    # return make_response(jsonify(f"Card #{card.card_id} successfully updated"))
    

