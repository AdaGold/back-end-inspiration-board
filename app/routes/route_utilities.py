from ..db import db
from flask import abort, make_response
# from sqlalchemy import inspect

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        response = {"message": f"{cls.__name__} {model_id} is invalid"}
        abort(make_response(response, 400))
    
    # cleaner option? use inspect to get primary key of class instead of hard coding board_id or card_id
    # primary_key = inspect(cls).primary_key[0]
    # query = db.select(cls).where(primary_key == model_id)

    mod_id = cls.board_id if cls.__name__ == "Board" else cls.card_id
    query = db.select(cls).where(mod_id == model_id)
    model = db.session.scalar(query) 
    if not model:
        response = {"message": f"{cls.__name__} {model_id} not found"}
        abort(make_response(response, 404)) 
    return model


def create_model(cls, model_data):
    try:
        new_model = cls.make_new(model_data)
    except KeyError as error:
        response = {"message": f"invalid {cls.__name__}: missing {error.args[0]}"}
        abort(make_response(response, 400))
    except:
        response = {"message": f"invalid {cls.__name__}: message cannot be empty or over 40 characters long"}
        abort(make_response(response, 400))        
    db.session.add(new_model)
    db.session.commit()
    return new_model.to_dict(), 201