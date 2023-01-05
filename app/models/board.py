from app import db

class Board(db.Model):
    board_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    owner = db.Column(db.String)
    cards = db.relationship("Card", back_populates="board")

    def create_board_dict(self):

        new_dict = {
            "board_id": self.board_id,
            "title": self.title,
            "owner": self.owner,
        }

        return new_dict