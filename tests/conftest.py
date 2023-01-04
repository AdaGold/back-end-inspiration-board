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

# @pytest.fixture
# def board_item(app):
#     new_board = Board(
#         title="Entry trial", owner="Alaere")
#     db.session.add(new_board)
#     db.session.commit()

@pytest.fixture
def select_second_board_item(app):
    db.session.add_all([
        Board(board_id=1, title="Entry trial 1", owner="Alaere"),
        Board(board_id=2, title="Entry trial 2", owner="Mia"),
        Board(board_id=3, title="Entry trial 3", owner="Anika")
    ])
    db.session.commit()