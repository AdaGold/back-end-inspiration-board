from app.models.card import Card
import pytest

# @pytest.mark.skip(reason="incomplete")
def test_no_cards_saved(client):
    # Act
    response = client.get("/cards")
    response_body = response.get_json()

    # Assert 
    assert response.status_code == 200
    assert response_body == []

# @pytest.mark.skip(reason="incomplete")
def test_get_cards_one_saved_card(client, one_card):
    # Act
    response = client.get("/cards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{
        'card_id': 1,
        'likes': 0,
        'message': 'Have a wonderful day'
    }]
    
# @pytest.mark.skip(reason="incomplete")
def test_get_card_that_does_not_exist(client, one_card):
    # Act
    response = client.get("/cards/2")
    response_body = response.get_json()
    # Assert 
    assert response.status_code == 404
    assert response_body == {
        'message': 'Card 2 does not exist'
    }

# @pytest.mark.skip(reason="incomplete")
def test_get_card_id_3(client, four_cards):
    # Act
    response = client.get("/cards/3")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == { "card" : {
        'card_id': 3,
        'likes': 12,
        'message': 'You are special'
        }
    }

def test_post_one_card(client):
    # Act 
    response = client.post("/cards", json={"card_id": 1, "likes": 0, "message": "New message"})
    response_body = response.get_json()

    # Assert 
    assert response_body == { "card" : {
        'card_id': 1,
        'likes': 0,
        "message": 'New message'
        }  
    }
    assert response.status_code == 201

def test_delete_one_card(client, four_cards):
    # Act
    response = client.delete("/cards/3")
    response_body = response.get_json()

    # Assert 
    assert response.status_code == 200
    assert 'details' in response_body
    assert response_body == {"details": 'Card 3 \"You are special\" successfully deleted'}
    assert Card.query.all() == [Card.query.get(1), Card.query.get(4), Card.query.get(5)]

def test_delete_card_not_found(client):
    # Act
    response = client.delete("/cards/15")
    response_body = response.get_json()
    # Assert
    assert response.status_code == 404
    assert Card.query.all() == []

def test_update_like_count(client, one_card):
    # Act 
    response = client.patch("cards/1", json={"likes": 0})
    response_body = response.get_json()
    # Assert 
    card = Card.query.get(1)
    assert response.status_code == 200
    assert response_body == { 'card': {
        "card_id": 1,
        "likes": 1,
        "message": "Have a wonderful day"
        }
    }
    assert card.likes == 1
