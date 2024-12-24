from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from ..db import db
from typing import Optional
from ..models.board import Board


class Card(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    message: Mapped[str]
    likes_count: Mapped[int]
    board_id: Mapped[Optional[int]] = mapped_column(ForeignKey("board.id"))
    board: Mapped[Optional["Board"]] = relationship(back_populates="cards")
