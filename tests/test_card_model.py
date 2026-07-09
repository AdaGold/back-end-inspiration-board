from app.models.card import Card


def test_to_dict():
    test_data = Card(card_id=1, message="hello", likes_count=0)
    result = test_data.to_dict()
    assert result["message"] == "hello"
    assert result["likes_count"] == 0
    assert result["id"] == 1