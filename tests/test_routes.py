from app.models.board import Board
import pytest

@pytest.mark.skip(reason="incomplete")
def test_get_boards_returns_empty_list(client):
    # Act
    response = client.get("/board")
    response_body = response.get_json()

    # Assert 
    assert response.status_code == 200
    assert response_body == []

# Write test to get all of the items on the board
@pytest.mark.skip(reason="incomplete")
def test_get_all_boards(client):
    pass

@pytest.mark.skip(reason="incomplete")
def test_get_one_board(client, board_item):
    pass


@pytest.mark.skip(reason="incomplete")
def test_post_message_on_board(client):
    pass


@pytest.mark.skip(reason="incomplete")
def test_delete_all_boards(client):
    pass





