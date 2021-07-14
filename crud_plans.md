# Must Ensure the following CRUD paths work:
~~- [ ] GET /boards~~

~~- [ ] POST /boards~~

- [ ] GET /boards/<board_id>/cards
- [ ] POST /boards/<board_id>/cards
- [ ] DELETE /cards/<card_id>
- [ ] PUT /cards/<card_id>/like


### 1. Get Boards: Getting saved Boards
- [ ] GET /boards

As a client, I want to be able to make a `GET` request to `/boards` when there is at least one but possibly many saved boards and get this response:
`200 ok`

```json
[
    {
        "board_id": 1,
        "title": "Literary Quotes",
        "owner": "Octavia Butler"
    },
    {
        "board_id": 2,
        "title": "Supreme Court Quotes",
        "owner": "Ruth Bader Ginsburg"
    },
    {
        "board_id": 3,
        "title": "Jokes",
        "owner": "Really Funny Person"
    }
]
```

### 2. Create a Board: (invalid if title or owner not included)
- [ ] POST /boards

As a client, I want to be able to make a `POST` request to `/boards` with the following HTTP request body


```json
{
    "title": "Brand New Board",
    "owner": "Marry Poppins"
}
```

and get this response:

`201 CREATED`

```json
{
    "board": {
        "board_id": 1,
        "title": "Brand New Board",
        "owner": "Marry Poppins"
    }
}
```
So that I know I succesfully created a Board that is saved in the databse.

### 3. Get Boards: No saved Boards
- [ ] GET /boards

As a client, I want to be able to make a `POST` request to `/boards` when there are zero saved tasks and get this response:
`200 ok`
```json
[]
```


### Get one Board: one saved Board
As a client, I want to be able to make a `GET` request to `/boards/1` when there is at least one saved board and get this response:

`200 ok`
```json
{
    "board": {
        "board_id": 1,
        "title": "New Board for me",
        "owner": "Spice Girls"
    }
}
```

### Get One Board: No matching Boards
As a client, I want to be able to make a `GET` request to `/boards/1` when there are no matching boards and get this response:

`404 Not Found`

No response body.

### Update Board
As a client, I want to be able to make a `PUT` request to `/boards/1` when there is at least one saved board with this request body:

```json
{
    "title": "New name for fancy board",
    "owner": "Morty"
}
```

and get this response:
`200 ok`
```json
{
    "board": {
        "board_id": 1,
        "title": "New name for fancy board",
        "owner": "Morty"
    }
}
```

### Update Board: No matching Board
As a client, I want to be able to make a `PUT` request to `/boards/2` when there are no matching tasks with this request body:

```json
{
    "title": "New title for board",
    "owner": "Trish"
}
```
and get this response:
`404 Not Found`
No response body

### Delete Board: Deleting a board

### Delete Board: No Matching Board

***
Need to decide on what circumstance will we not allow a database creation to begin.
- example 
-- when no title is provided?
-- when no owner is provided?

### Create a Board: Invalid Board With Missing Data **

<hr />

# Need to go through crud for Cards like I did for board above.

### Create a Card: valid card

### Get Cards: Getting saved cards

### Get Cards: No saved Cards

### Get One Card: One saved Card

### Get One Card: No matching Card

### Update Card:

### Update Card: No matching Card

### Delete Card: Deleting a Card

### Delete Card: No matching Card

### Create a Card: Invalid Card with missing data


