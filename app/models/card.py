from app import db
from flask import current_app

class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)
    likes_count = db.Column(db.Integer, default=0)
    
    #create relationship
    board_id = db.Column(db.Integer, db.ForeignKey('board.board_id'))
    
    # def to_json_card(self):
        
    #     return {
    #             "board":  
    #                 {   "card_id" :self.card_id,
    #                     "board_id": self.board_id,
    #                     "message": self.message,
    #                     "likes_count": self.likes_count
    #                } 
    #     }
    
    def to_json_no_key(self):
       return  {    "card_id" :self.card_id,
                    "board_id": self.board_id,
                    "message": self.message,
                    "likes_count": self.likes_count
                   } 
    
    @staticmethod
    def from_json(card_json):
        return Card(message=card_json["message"])
        
        #likes_count=card_json["likes_count"])
    