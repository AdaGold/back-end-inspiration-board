from app import db

class Board(db.Model):
    board_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner = db.Column(db.String)
    title = db.Column(db.String)
    cards = db.relationship("Card", back_populates="board")


    def to_dict(self):
        return {
            "board_id" : self.board_id,
            "owner": self.owner,
            "title": self.title,
        }
        
    @classmethod
    def create_board(cls, board_data):
        return cls(owner=board_data["owner"], title=board_data["title"])

