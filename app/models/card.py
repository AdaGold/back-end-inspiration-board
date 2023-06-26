from app import db

class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    likes = db.Column(db.Integer)
    message = db.Column(db.String)
    board_id = db.Column(db.Integer, db.ForeignKey('board.board_id'))
    board = db.relationship("Board", back_populates="cards")

    def to_dict(self):
            card_dict = {
                "card_id" : self.card_id,
                "likes": self.likes,
                "message": self.message,
            }

            return card_dict

    @classmethod
    def from_dict(cls, card_data):
        return Card(likes=card_data["likes"],message=card_data["message"])