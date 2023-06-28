from app import db

class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)
    likes_count = db.Column(db.Integer, default= 0)
    board_id = db.Column(db.Integer, db.ForeignKey('board.board_id'), nullable=True)

    def card_to_json(self):
        return {
            "card_id": self.card_id,
            "message": self.message,
            "likes_count": self.likes_count
        }