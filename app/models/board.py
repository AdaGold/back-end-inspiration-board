from sqlalchemy.orm import backref
from app import db

class Board(db.Model):
    board_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    owner = db.Column(db.String)
    cards = db.relationship("Card", backref="board", lazy=True)
    # not sure if we actually need cards here. 
    # sort of like we had tasks.