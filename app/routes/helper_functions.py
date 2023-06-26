from flask import jsonify, abort, make_response

def get_one_obj_or_abort(cls, id):
    try:
        id = int(id)
    except ValueError:
        response = f"ID must be an integer. '{id}' not valid"
        abort(make_response(jsonify({"msg": response}), 400))

    obj = cls.query.get(id)

    if not obj:
        response = f"{cls.__name__} with ID {id} not found"
        abort(make_response(jsonify({"msg": response}), 404))

    return obj