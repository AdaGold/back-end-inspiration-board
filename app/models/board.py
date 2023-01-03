from app import db

class Board(db.Model):
    board_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner = db.Column(db.String)
    title = db.Column(db.String)

    def create_board(board_data):
        return Board(owner=board_data["owner"], title=board_data["title"])

