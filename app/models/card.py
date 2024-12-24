from sqlalchemy.orm import Mapped, mapped_column,relationship
from ..db import db

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .board import Board

class Card(db.Model):
    card_id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    message: Mapped[str] 
    likes_count: Mapped[int] 
    board_id:Mapped[int] = mapped_column(foreign_key="board.board_id")
    board: Mapped["Board"] = relationship(back_populates="cards")

    def to_dict(self):
        return {
            "card_id": self.card_id,
            "message": self.message,
            "likes_count": self.likes_count,
            "board_id": self.board_id
        } 