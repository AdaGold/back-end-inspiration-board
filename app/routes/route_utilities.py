from flask import abort, make_response
from ..db import db


def validate_model(cls, model_id):
    model_id = int(model_id)
    query = db.select(cls).where(cls.id == model_id)
    model = db.session.scalar(query)
    if not model:
        raise Exception("model not found")
    return model
