import json
from flask import Response
from app import app

@app.errorhandler(401)
def unauth(e):
    err = json.dumps({'error' : e})
    return Response(err, status=401, mimetype='application/json')

@app.errorhandler(405)
def bad_method(e):
    err = json.dumps({'error' : 'bad method'})
    return Response(err, status=405, mimetype='application/json')

@app.errorhandler(400)
def bad_request(e):
    err = json.dumps({'error' : e})
    return Response(err, status=400, mimetype='application/json')

def bad_json():
    return bad_request('bad json')
