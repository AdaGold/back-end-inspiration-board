import pytest
from app import create_app
from app.db import db
from flask.signals import request_finished
from dotenv import load_dotenv
import os
from app.models.board import Board
from app.models.card import Card

load_dotenv()

@pytest.fixture
def app():
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    }
    app = create_app(test_config)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def one_board(app):
    new_board = Board(title="First Board", owner="First Owner")
    db.session.add(new_board)
    db.session.commit()

@pytest.fixture
def many_boards(app):
    boards_list = [Board(title="First Board", owner="First Owner"),
                       Board(title="Second Board", owner="Betty"),
                       Board(title="Third Board", owner="Charlie"),
                       Board(title="Fourth Board", owner="Debbie"),
                       Board(title="Fifth Board", owner="Eddie")]
    db.session.add_all(boards_list)
    db.session.commit()

@pytest.fixture
def one_card(app):
    new_card = Card(message="new message", board_id=1) 
    db.session.add(new_card)
    db.session.commit()

@pytest.fixture
def many_cards(app):
    cards_list = [Card(message="new message", board_id=1),
                  Card(message="second message", board_id=1), 
                  Card(message="third message", board_id=1),
                  Card(message="fourth message", board_id=1), 
                  Card(message="fifth message", board_id=1)] 
    db.session.add_all(cards_list)
    db.session.commit()

# #may be unneeded
# @pytest.fixture
# def many_cards_many_boards(app):
#     # cards_list = [Card(message="new message", board_id=1),
#     #               Card(message="second message", board_id=1), 
#     #               Card(message="msg for second board", board_id=2),
#     #               Card(message="another msg for second board", board_id=2), 
#     #               Card(message="msg for third board message", board_id=3)] 
#     # db.session.add_all(cards_list)
#     # db.session.commit()
#     cards_list_1 = [Card(message="new message", board_id=1),
#                   Card(message="second message", board_id=1)] 
#     db.session.add_all(cards_list_1)
#     # db.session.commit()
#     cards_list_2 = [Card(message="msg for second board", board_id=2),
#                   Card(message="another msg for second board", board_id=2)] 
#     db.session.add_all(cards_list_2)
#     db.session.commit()