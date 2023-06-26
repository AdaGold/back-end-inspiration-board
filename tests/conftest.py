import pytest
from app import create_app
from app.models.board import Board
from app.models.card import Card
from app import db


@pytest.fixture
def app():
    # create the app with a test config dictionary
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    # close and remove the temporary database
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def one_board(app):
    new_board = Board(board_id=1, title="Entry trial", owner="Alaere")
    db.session.add(new_board)
    db.session.commit()
    return new_board

@pytest.fixture
def three_board_items(app):
    db.session.add_all([Board(board_id=1, title="Entry trial 1", owner="Alaere"),
        Board(board_id=2, title="Entry trial 2", owner="Mia"),
        Board(board_id=3, title="Entry trial 3", owner="Anika")
    ])
    db.session.commit()

@pytest.fixture
def one_card(app):
    new_card = Card(likes=0, message="Have a wonderful day")
    db.session.add(new_card)
    db.session.commit()
    return new_card


@pytest.fixture
def four_cards(app):
    new_card = [Card(card_id=1, likes=0, message="Have a wonderful day"), 
    Card(card_id=3, likes=12, message="You are special"), 
    Card(card_id=4, likes=8, message="You got this!!"),
    Card(card_id=5, likes=19, message="An apple a day keeps the doctors away")
    ]

    db.session.add_all(new_card)
    db.session.commit()

@pytest.fixture
def one_card_belongs_to_one_board(app, one_board, one_card):
    new_board = Board(board_id=6, title="Entry trial 6", owner="Nancy")
    card = Card(likes=0, message="Have a wonderful day")
    new_board.cards.append(card)
    db.session.add(new_board)
    db.session.commit()

    return new_board





