
#tests for delete_card
def test_delete_card_returns_card_works_not_found(client, one_board, many_cards):
    response = client.delete("/cards/3")
    assert response.status_code == 200
    assert response.get_json() == {"message": f"Card 3 deleted"}


def test_delete_card_returns_invalid(client, one_board, many_cards):
    response = client.delete("/cards/three")
    assert response.status_code == 400
    assert response.get_json() == {"message": "Card three is invalid"}


#tests for update_card
def test_update_card_likes_increases_like_by_one(client, one_board, many_cards):
    response = client.put("/cards/3/likes")
    assert response.status_code == 200
    assert response.get_json()["likes_count"] == 1


def test_update_card_likes_returns_invalid(client, one_board, many_cards):
    response = client.put("/cards/three/likes")
    assert response.status_code == 400
    assert response.get_json() == {"message": "Card three is invalid"}


def test_update_card_returns_card_not_found(client, one_board, many_cards):
    response = client.put("/cards/17/likes")
    assert response.status_code == 404
    assert response.get_json() == {"message": "Card 17 not found"}