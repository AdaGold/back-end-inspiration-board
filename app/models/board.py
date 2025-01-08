from sqlalchemy.orm import Mapped, mapped_column,relationship
from ..db import db

class Board(db.Model):
    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] 
    owner: Mapped[str] 

    cards = relationship("Card", back_populates="board")

    def to_dict(self):
      
        board_dict ={
            "id": self.id,
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
