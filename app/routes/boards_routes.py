from flask import Blueprint, jsonify, request
from app import db
from app.models.board import Board
import os

board_bp = Blueprint("board_bp", __name__, url_prefix="/boards")