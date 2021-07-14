from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.board import Board
from app.models.card import Card
import os
from dotenv import load_dotenv

boards_bp = Blueprint("boards", __name__, url_prefix="/boards")
hello_world_bp = Blueprint("hello_world", __name__)


load_dotenv()


@hello_world_bp.route("/hello-world", methods=["GET"])
def hello_world():
    my_beautiful_response_body = "Hello, World!"
    return my_beautiful_response_body

# def post_message_to_slack(text):
#     SLACK_TOKEN = os.environ.get('SLACKBOT_TOKEN')
#     slack_path = "https://slack.com/api/chat.postMessage"
#     query_params = {
#         'channel': 'team-duck-yeah',
#         'text': text
#     }
#     headers = {'Authorization': f"Bearer {SLACK_TOKEN}"}
#     request.post(slack_path, params=query_params, headers=headers)


@boards_bp.route("", methods=["GET", "POST"])
def handle_boards():
    if request.method == "GET":
        boards = Board.query.all()
        boards_response = []
        for board in boards:
            boards_response.append({
                "board_id": board.board_id,
                "title": board.title,
                "owner": board.owner,
            })
        return jsonify(boards_response)
    elif request.method == "POST":
        request_body = request.get_json()
        title = request_body.get("title")
        owner = request_body.get("owner")
        new_board = Board(title=request_body["title"],
                          owner=request_body["owner"])
        db.session.add(new_board)
        db.session.commit()

    return make_response(f"Board {new_board.title} successfully created", 201)


@boards_bp.route("/<board_id>", methods=["GET", "PUT", "DELETE"])
def handle_board(board_id):
    board = Board.query.get(board_id)

    if request.method == "GET":
        if board == None:
            return make_response("That board does not exist", 404)
        return {
            "id": board.board_id,
            "title": board.title,
            "owner": board.owner,
            "cards": board.cards
        }
    elif request.method == "PUT":
        if board == None:
            return make_response("Board does not exist", 404)
        form_data = request.get_json()

        board.title = form_data["title"]
        board.owner = form_data["owner"]

        db.session.commit()

        return make_response(f"Board: {board.title} sucessfully updated.")

    elif request.method == "DELETE":
        if board == None:
            return make_response("Board does not exist", 404)
        db.session.delete(board)
        db.session.commit()
        return make_response(f"Board: {board.title} sucessfully deleted.")
# example_bp = Blueprint('example_bp', __name__)


@boards_bp.route("/<board_id>/cards", methods=["POST", "GET"])
def handle_cards(board_id):
    board = Board.query.get(board_id)

    if board is None:
        return make_response("", 404)

    if request.method == "GET":
        cards = Board.query.get(board_id).cards
        cards_response = []
        for card in cards:
            cards_response.append({
                "message": card.message
            })

        return make_response(
            {
                "cards": cards_response
            }, 200)
    elif request.method == "POST":
        request_body = request.get_json()
        if 'message' not in request_body:
            return {"details": "Invalid data"}, 400
        new_card = Card(message=request_body["message"],
                        board_id=board_id)

        db.session.add(new_card)
        db.session.commit()

        return {
            "card": {
                "id": new_card.card_id,
                "message": new_card.message
            }
        }, 201
