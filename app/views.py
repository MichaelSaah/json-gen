from jsongen import JsonGen
from flask import Flask, request, Response, jsonify
from app.models import User, Transaction
from datetime import datetime
from app.decorators import require_key
from app.errors import unauth, bad_request, bad_json
import json

from app import app, db

jg = JsonGen()


@require_key
def api_view(request, user):
    try:
        data = json.loads(request.data.decode('utf-8'))
    except json.JSONDecodeError:
        return bad_json()

    # validate fields
    if 'model' not in data:
        return bad_request("No `model` prodivded in request")
    model = data['model']

    if 'n' in data:
        try:    
            n = int(data['n'])
        except ValueError:
            return bad_request("Value given for `n` is not valid: " + str(data['n']))
        if n < 1:
            return bad_request("Value given for `n` is less than 1")
    else:
        n = 1

    if 'refresh' in data:
        refresh = data['refresh']
        if type(refresh) is not bool:
            return bad_request("Value given for `refresh` is not valid: " + str(refresh))
    else:
        refresh = True

    # do transaction
    record = json.dumps({'model': model, 'n': n})
    last_trans = Transaction.query.filter_by(request=record, user=user).first()

    if refresh or last_trans is None:
        # TODO deal with bad model
        data_out, cost = jg.generate(model, n)    
        response = json.dumps(data_out)    
        transaction = Transaction(user=user, 
                                  cost=cost,
                                  request=record,
                                  response=response,
                                  time=datetime.now())
    else:
        response = last_trans.response
        transaction = Transaction(user=user,
                                  cost=last_trans.cost,
                                  request=record,
                                  response=last_trans.response,
                                  time=datetime.now())

    db.session.add(transaction)
    db.session.commit()
    
    return response
