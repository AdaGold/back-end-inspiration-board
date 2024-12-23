from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Board(db.Model):
    board_id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] 
    owner: Mapped[str] 

    def to_dict(self):
      
        board_dict ={
            "board_id": self.board_id,
            "title": self.title,
            "owner": self.owner
        }
        return board_dict

    @classmethod
    def from_dict(cls, board_data):
        return cls(
            title=board_data["title"],
            owner=board_data["owner"]
        )
