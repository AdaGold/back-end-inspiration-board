from app.models.card import Card
import pytest

@pytest.mark.skip(reason="incomplete")
def test_no_cards_saved(client):
    # Act
    response = client.get("/cards")
    response_body = response.get_json()

    # Assert 
    assert response.status_code == 200
    assert response_body == []

@pytest.mark.skip(reason="incomplete")
def test_get_cards_one_saved_card(client, one_card):
    # Act
    response = client.get("/cards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{
        {
            "card_id": None,
            "likes": None, 
            "message": None,
        }
    }
    ]

@pytest.mark.skip(reason="incomplete")
def test_get_card(client, one_card):
    # Act
    response = client.get("/cards/1")
    response_body = response.get_json()

    # Assert 

# @pytest.mark.skip(reason="incomplete")