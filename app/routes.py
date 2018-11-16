from jsongen.processors import build_data_out, calculate_cost
from flask import Flask, request, Response
from app.models import User, Transaction
from datetime import datetime
import json

from app import app, db

@app.route('/')
def index():
    return 'index'

@app.route('/api/', methods=['POST'])
def api():
    # TODO: check mimetype
    # TODO: establish who exactly can raise Key and Value errors in process_json
    try:
        data = json.loads(request.data.decode('utf-8'))
    except json.JSONDecodeError as e:
        return bad_request(e)

    # validate model, n, user
    if 'model' not in data:
        return bad_request("No `model` prodivded in request")
    model = data['model']

    if 'n' not in data:
        return bad_request("No `n` provided in request")
    try:    
        n = int(data['n'])
    except ValueError:
        return bad_request("Value given for `n` is not valid: " + str(data['n']))
    
    if 'user' not in data:
        return bad_request("No `user` provided in request")
    user = User.query.filter_by(username=data['user']).first()
    if user is None:
        return bad_request("Provided user does not exist")

    cost = n * calculate_cost(model)
    record = json.dumps({'model': model, 'n': n})
    
    data_out = build_data_out(model, n)
    data_out_as_json = json.dumps(data_out)
    
    transaction = Transaction(user=user, cost=cost, request=record, time = datetime.now())
    db.session.add(transaction)
    db.session.commit()

    return data_out_as_json

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

