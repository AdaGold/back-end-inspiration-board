from flask import Blueprint, request, jsonify, make_response, Response
from app import db
from .models.card import Card
from .models.board import Board
from sqlalchemy import desc, asc

# example_bp = Blueprint('example_bp', __name__)
card_bp = Blueprint("/board/<board_id>/cards", __name__, url_prefix="/board/<board_id>/cards")

@card_bp.route("", methods=["POST"], strict_slashes=False)
def create_a_card(board_id):
    
    board = Board.query.get(board_id)
    #print(f"##### {board_id} #####")
    
    if not board or board == None:
        return jsonify(""), 404 
   
    request_body = request.get_json()

    if len(request_body["message"]) > 40:
        return jsonify(details="character limit exeeded"), 400
    
    if "message" not in request_body or len(request_body["message"]) == 0:
        return jsonify(details="invalid data"), 400
    
    new_card  = Card.from_json(request_body)
    new_card.board_id = board_id
    
    #print(f"create_a_card card.boardId: {new_card.board_id}")
    
    db.session.add(new_card)
    db.session.add(board)
    db.session.commit()
    return make_response(new_card.to_json(), 201)


@card_bp.route("", methods=["GET"], strict_slashes=False)
def get_all_cards(board_id):
    
    # get sort query param
    sort_by_like_count_order = request.args.get("sort");
    
    # board = Board.query.get(board_id)
    
    #print(f"get_all_cards(): Board = {board}")
    
    #if not board or board == None:
    #    return jsonify(""), 404 
    
    cards_list = []
    
    # board_cards = board.cards
    
    #print(f"get_all_cards(): board.cards = {board_cards}")
    
    # for card in board.cards:
    #     card_data = Card.query.get(card.card_id)
    #     cards_list.append(card_data.to_json())
    
    if sort_by_like_count_order is not None:
        if (sort_by_like_count_order == "asc"):
            cards_list = db.session.query(Card).filter_by(board_id=board_id).order_by(asc(Card.likes_count)) 
        else:
            cards_list = db.session.query(Card).filter_by(board_id=board_id).order_by(desc(Card.likes_count))
    else:
        cards_list = db.session.query(Card).filter_by(board_id=board_id).all()
    
    cards_json_list = [ card.to_json() for card in cards_list ]
    
    return make_response(jsonify(cards_json_list), 200)         


@card_bp.route("<card_id>", methods=["DELETE"], strict_slashes=False)
def delete_a_card(board_id, card_id):

    card = Card.query.get(card_id)

    if card == None:
        return Response("",status=404)

    if card:
        db.session.delete(card)
        db.session.commit()

    return jsonify(id=int(card_id)), 200


@card_bp.route("<card_id>", methods=["PUT"], strict_slashes=False)
def like_a_card(board_id, card_id):
    card = Card.query.get(card_id)

    if card == None:
        return Response("",status=404)
    
    card.likes_count += 1
    
    db.session.add(card)
    db.session.commit()
    
    return card.to_json(), 200