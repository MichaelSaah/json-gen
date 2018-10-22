from json_gen.gen import build_data_out, process_json
from flask import Flask, request, Response, abort
import json

app = Flask(__name__)


@app.route('/', methods=['POST'])
def handler():
    try:
        model, n = process_json(request.data)
    except json.JSONDecodeError as e:
        return bad_request(e)
    except KeyError as e:
        return bad_request(e)
    except ValueError as e:
        return bad_request(e)

    data_out = build_data_out(model, n)
    data_out_as_json = json.dumps(data_out)
    return data_out_as_json

@app.errorhandler(405)
def bad_method(e):
    err = json.dumps({'error' : 'requests must be made via POST'})
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

if __name__=="__main__":
    app.run(host='0.0.0.0')
