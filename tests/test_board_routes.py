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
def test_get_all_boards(client, three_board_items):
    # Act
    response = client.get("/boards")
    response_body = response.get_json()

    # Assert 
    assert response.status_code == 200
    assert "boards" in response_body
    # assert response_body == {
    #     "boards" : {

    #     }
    # }

# @pytest.mark.skip(reason="incomplete")
def test_get_one_board(client, three_board_items):
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
    # assert response_body == "New board successfully created"

# @pytest.mark.skip(reason="incomplete")
def test_delete_all_boards(client, three_board_items):
    # Act
    response = client.delete("/boards")
    response_body = response.get_json()

    # Assert 
    assert response.status_code == 200
    assert Board.query.all() == []
    assert response_body == {"details": "Boards successfully deleted"}


def test_delete_board_by_id(client, three_board_items):
    # Act 
    response = client.delete("/boards/1")
    response_body = response.get_json()

    # Assert 
    assert response.status_code == 200
    assert 'details' in response_body
    assert response_body == {
        "details": 'Board 1 "Entry trial 1" successfully deleted'
    }
    assert Board.query.get(1) == None

# @pytest.mark.skip(reason="incomplete")








