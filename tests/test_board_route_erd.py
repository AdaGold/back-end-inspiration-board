from app.models.board import Board
from app.models.card import Card
from app import db
import pytest

def test_post_card_to_board(client, one_card, one_board):
    # Act 
    response = client.post("/boards/1/cards", json={
        'card_id': 2,
        'likes': 0,
        'message': 'Have a wonderful day'
    })

    response_body = response.get_json()

    # Assert 
    assert response.status_code == 201
    assert response_body == {
        "board_id": 1,
        "cards": {"card_id": 2, 'likes': 0, 'message': 'Have a wonderful day'
        },
    }
    assert len(Board.query.get(1).cards) == 1


def test_get_cards_for_specific_board_cards(client, one_card_belongs_to_one_board):
    # Act
    response = client.get("/boards/6/cards")
    response_body = response.get_json()

    # Assert 
    assert response.status_code == 200
    assert 'cards' in response_body
    assert response_body == {
        'board_id': 6,
        'cards': [{'card_id': 2, 'likes': 0, 'message': 'Have a wonderful day'}]
    }

# def test_delete_all_cards_from_board(client, one_card, one_board):
#     card = one_card.likes
#     print(card)
#     print(one_board())
#     # Act
#     response = client.delete(f"/board/1/cards")
#     assert response.status_code == 200
#     assert f"All cards from board" in response.data

#     # Check that the card has been deleted from the board


def test_delete_all_cards_from_board(client, one_board, one_card):
    # Create a card and associate it with the board
    one_card.board_id = one_board.board_id
    db.session.add(one_card)
    db.session.commit()

    # Make a DELETE request to the endpoint
    response = client.delete(f"/boards/{one_board.board_id}/cards")
    assert response.status_code == 200
    assert b"All cards from board" in response.data

    # Check that the card has been deleted from the board
    cards = Card.query.filter_by(board_id=one_board.board_id).all()
    assert len(cards) == 0

def test_delete_all_cards_from_board_with_no_cards(client, one_board):
    #Make a DELETE request to the endpoint
    response = client.delete(f"/boards/{one_board.board_id}/cards")

    assert response.status_code == 404
    assert b"No cards found" in response.data
