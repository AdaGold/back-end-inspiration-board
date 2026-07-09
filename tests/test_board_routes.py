
# tests for get_all_boards()
def test_get_all_boards_with_no_boards(client):
    response = client.get("/boards")

    assert response.status_code == 200
    assert response.get_json() == []


def test_get_all_boards_with_one_board(client, one_board):
    response = client.get("/boards")
    # response_body = request.get_json()

    assert response.status_code == 200
    assert response.get_json() == [{"id": 1, "title": "First Board", "owner": "First Owner"}]
    assert len(response.get_json()) == 1


def test_get_all_boards_with_many_boards(client, many_boards):
    response = client.get("/boards")

    assert response.status_code == 200
    assert response.get_json() == [{"id": 1, "title": "First Board", "owner": "First Owner"}, 
                                   {"id": 2, "title": "Second Board", "owner": "Betty"},
                                   {"id": 3, "title": "Third Board", "owner": "Charlie"},
                                   {"id": 4, "title": "Fourth Board", "owner": "Debbie"},
                                   {"id": 5, "title": "Fifth Board", "owner": "Eddie"},
                                   ]
    assert len(response.get_json()) == 5


#tests for get_one_board()
def test_get_one_board_returns_specific_board_of_many(client, many_boards):
    response = client.get("/boards/2")

    assert response.status_code == 200
    assert response.get_json() == {"id": 2, "title": "Second Board", "owner": "Betty"}


def test_get_one_board_returns_another_board_of_many(client, many_boards):
    response = client.get("/boards/4")

    assert response.status_code == 200
    assert response.get_json() == {"id": 4, "title": "Fourth Board", "owner": "Debbie"}


def test_get_one_board_invalid_id(client, many_boards):
    response = client.get("/boards/one")

    assert response.status_code == 400
    assert response.get_json() == {"message": "Board one is invalid"}


def test_get_one_board_nonexistent_id_of_many(client, many_boards):
    response = client.get("/boards/17")

    assert response.status_code == 404
    assert response.get_json() == {"message": "Board 17 not found"}


def test_get_one_board_nonexistent_id_of_none(client):
    response = client.get("/boards/1")

    assert response.status_code == 404
    assert response.get_json() == {"message": "Board 1 not found"}


#tests for make_new_board()
def test_make_new_board_successfully(client):
    response = client.post("/boards", json={"title": "Shire", "owner": "Frodo"})

    assert response.status_code == 201
    assert response.get_json() == {"id": 1, "title": "Shire", "owner": "Frodo"}
   

#tests for get_cards()
def test_get_cards_when_one_card_exists(client, one_board, one_card):
    response = client.get("/boards/1/cards")

    assert response.status_code == 200
    assert response.get_json()[0]["message"] == "new message"
    assert response.get_json()[0]["board_id"] == 1


def test_get_cards_when_many_cards_exist(client, one_board, many_cards):
    response = client.get("/boards/1/cards")

    assert response.status_code == 200
    
    assert len(response.get_json()) == 5
    assert response.get_json()[0]["message"] == "new message"
    assert response.get_json()[0]["board_id"] == 1
    assert response.get_json()[1]["message"] == "second message"
    assert response.get_json()[1]["board_id"] == 1
    assert response.get_json()[2]["message"] == "third message"
    assert response.get_json()[2]["board_id"] == 1
    assert response.get_json()[3]["message"] == "fourth message"
    assert response.get_json()[3]["board_id"] == 1
    assert response.get_json()[4]["message"] == "fifth message"
    assert response.get_json()[4]["board_id"] == 1


def test_get_cards_when_no_cards(client, one_board):
    response = client.get("/boards/1/cards")

    assert response.status_code == 200
    assert response.get_json() == []
    

#tests for make_new_card()
def test_make_new_card_successfully(client, one_board):
    response = client.post("/boards/1/cards", json={"message": "new message", "board_id": 1})

    assert response.status_code == 201
    assert response.get_json()["message"] == "new message"
    assert response.get_json()["board_id"] == 1 


def test_make_new_card_missing_message_error(client, one_board):
    response = client.post("/boards/1/cards", json={"board_id": 1})
    assert response.status_code == 400
    assert response.get_json() == {"message": "invalid Card: missing message"}


def test_make_new_card_too_long_error(client, one_board):
    response = client.post("/boards/1/cards", json={"message": "This is an example of a string that's too long", "board_id": 1})

    assert response.status_code == 400
    assert response.get_json() == {"message": 
                                   "invalid Card: message cannot be empty or over 40 characters long"} 

def test_make_new_card_empty_message_error(client, one_board):
    response = client.post("/boards/1/cards", json={"message": "", "board_id": 1})

    assert response.status_code == 400
    assert response.get_json() == {"message": 
                                   "invalid Card: message cannot be empty or over 40 characters long"} 