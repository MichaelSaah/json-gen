from jsongen import JsonGen
from flask import Flask, request, Response, jsonify
from app.models import User, Transaction
from datetime import datetime
import json

from app import app, db

jg = JsonGen()

def api_view(request):
    try:
        data = json.loads(request.data.decode('utf-8'))
    except json.JSONDecodeError as e:
        return bad_request(e)

    # validate model, n, user
    if 'model' not in data:
        return bad_request("No `model` prodivded in request")
    model = data['model']

    if 'user' not in data:
        return bad_request("No `user` provided in request")
    user = User.query.filter_by(username=data['user']).first()
    if user is None:
        return bad_request("Provided user does not exist")

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

    record = json.dumps({'model': model, 'n': n})
    last_trans = Transaction.query.filter_by(request=record).first()

    if refresh or last_trans is None:
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

@app.errorhandler(405)
def bad_method(e):
    err = json.dumps({'error' : 'bad method'})
    return Response(err, status=405, mimetype='application/json')

@app.errorhandler(400)
def bad_request(e):
    if isinstance(e, KeyError):
        key = str(e).replace("'", "")
        msg = '<' + key + "> not found"
    elif isinstance(e, json.JSONDecodeError):
        msg = "bad json: " + str(e)
    else:
        msg = str(e)
    err = json.dumps({'error' : msg})
    return Response(err, status=400, mimetype='application/json')

