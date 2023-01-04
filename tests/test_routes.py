from app.models.board import Board
import pytest

# @pytest.mark.skip(reason="incomplete")
def test_get_boards_returns_empty_list(client):
    # Act
    response = client.get("/boards")
    response_body = response.get_json()

    # Assert 
    assert response.status_code == 200
    assert response_body == []

# Write test to get all of the items on the board
@pytest.mark.skip(reason="incomplete")
def test_get_all_boards(client):
    pass

# @pytest.mark.skip(reason="incomplete")
def test_get_one_board(client, select_second_board_item):
    # Act 
    response = client.get("/boards/2")
    response_body = response.get_json()

    #Assert 
    assert response.status_code == 200
    assert "boards" in response_body
    assert response_body == {
        "boards": {
            "board_id": 2,
            "owner": "Mia",
            "title": "Entry trial 2"
        }
    }

def test_post_message_on_board(client):
    # Act
    response = client.post("/boards", json={
        "title": "Trial title",
        "owner": "Alaere",
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert "boards" in response_body
    assert response_body == {
        "boards": {
            "board_id": 1,
            "title": "Trial title",
            "owner": "Alaere",
        }
    }
    new_board = Board.query.get(1)
    assert new_board


@pytest.mark.skip(reason="incomplete")
def test_delete_all_boards(client):
    pass





