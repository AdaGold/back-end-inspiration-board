from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db

class Board(db.Model):
    board_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    owner: Mapped[str]
    cards: Mapped[list["Card"]] = relationship(back_populates="board")

    def to_dict(self):
        board_dict = {"id":self.board_id, "title": self.title, "owner": self.owner}
        return board_dict
    
    @classmethod
    def make_new(cls, dict):
        new_book = cls(title=dict["title"], owner=dict["owner"])
        return new_book
