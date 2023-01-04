from app import db

class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String)
    likes_count = db.Column(db.Integer)

    def create_dict(self):

        new_dict = {
            "card_id": self.card_id,
            "message": self.message,
            "likes_count": self.likes_count
        }

        return new_dict