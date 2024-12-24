from flask import Blueprint, abort, make_response, request, Response
from app.models.card import Card
from ..db import db
import json
import os

cards_bp = Blueprint("cards_bp", __name__, url_prefix="/cards")


@cards_bp.post("")
def create_card():
    pass
