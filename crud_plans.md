# CRUD Operations for the Inspo Board backend API
- You will need to replace the <board_id>s and <card_ids>s for your own usecases.

# Handling Boards
### Post --> Create a new Board
- `/boards`
- `https://inspo--board.herokuapp.com/boards`

Example Payload body:
```json
{
    "title": "Arizona",
    "owner": "TrishTheDish"
}
```
Endpoint will not let you create a board without a title or owner. It will give you an error message alerting you to this fact.

***
### PUT --> Edit a board by ID
- `/boards/<board_id>`
- `https://inspo--board.herokuapp.com/boards/2`

Example Payload body:
```json
{
    "owner": "Rudy G",
    "title": "Lumber is a board."
}
```
Endpoint will not let you edit a board that doesn't exist. Will give you helpful message if the board doesn't exist.

***
### DEL --> Delete a board by ID
- `/boards/<board_id>`
- `https://inspo--board.herokuapp.com/boards/3`

Endpoint will not let you delete a board that doesn't exist. Will give you a helpful message if board doesn't exist.

***
### GET --> Get a board by ID
- `/boards/<board_id>`
- `https://inspo--board.herokuapp.com/boards/2`

Endpoint will not let you get board that doesn't exist. Will give you helpful message if board doesn't exist.

***
### GET --> Get all The Boards if any exist
- `/boards`
- `https://inspo--board.herokuapp.com/boards`

If no boards exist then it will return an empty array.


# Handling Cards
### Post --> creating new card for a particular board.
- `boards/<board_id>/cards`
- `https://inspo--board.herokuapp.com/boards/2/cards`

Example Payload body:
```json
{
    "message": "here is a lovely quote for you to post"
}
```
***
### GET --> Get All Cards associated with a particular board.
- `/boards/<board_id>/cards`
- `https://inspo--board.herokuapp.com/boards/2/cards`

***
### Get --> Get card by ID
- `/cards/<card_id>`
- `https://inspo--board.herokuapp.com/cards/9`
***

### DEL --> Delete a card ny ID
- `/cards/<card_id>`
- `https://inspo--board.herokuapp.com/cards/9`
***
### PUT --> Edit card by ID
- `/cards/<card_id>`
- `http://127.0.0.1:5000/cards/8`

```json
{
    "message": "editing it one more time"
}
```

# Handle Likes
### Put --> Increase Likes Count by 1
- `/cards/<card_id>/like`
- `https://inspo--board.herokuapp.com/cards/9/like`