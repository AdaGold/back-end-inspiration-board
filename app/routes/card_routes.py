from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.card import Card
from app.models.board import Board


card_bp = Blueprint('card', __name__, url_prefix="/cards")

#Helper function
def valid_int(number):
    try:
        return int(number)     
    except:
        abort(make_response({"error": f"{number} must be an int"}, 400))
#Helper function
def get_card_from_id(card_id):
   card_id = valid_int(card_id)
   card = Card.query.get(card_id)

   if card:
        return card
   else:
        abort(make_response({"description": "Card not found"}, 404))


@card_bp.route("/<card_id>/like", methods =["PUT", "PATCH"])
def update_card_likes( card_id):
    # request_body = request.get_json()
    card = get_card_from_id(card_id)
    # if "likes_count" not in request_body:
    #     return jsonify("Incomplete data"), 400

    # card.likes_count = request_body["likes_count"]
    card.likes_count = card.likes_count + 1
   
    db.session.commit()

    return make_response(f"Card with id {card.card_id} has been updated. It has {card.likes_count} likes.", 200)


@card_bp.route("/<card_id>", methods=["DELETE"])
def delete_card(card_id):
    selected_card = Card.query.get(card_id)

    db.session.delete(selected_card)
    db.session.commit()

    return make_response(f"Card '{selected_card.card_id}' has been deleted", 200)