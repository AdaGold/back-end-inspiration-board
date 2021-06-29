from app import db

class Board(db.Model):
    board_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    owner = db.Column(db.String)

    def get_return(self):
        return{
                    "board_id": self.board_id,
                    "title": self.title,
                }
