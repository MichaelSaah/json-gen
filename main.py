from json_gen.gen import build_data_out, process_json
from flask import Flask, request, abort
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handler():
    data_in = request.data
    data_in = data_in.decode('utf8')
    model, n = process_json(data_in)
    data_out = json.dumps(build_data_out(model, n))
    return data_out

@app.errorhandler(405)
def bad_method(error):
    return "Requests must be made via POST", 405

if __name__=="__main__":
    app.run(host='0.0.0.0')
