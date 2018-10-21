from json_gen.gen import build_data_out, process_json
from flask import Flask, request, abort
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handler():
    model, n = process_json(request.data)
    data_out = build_data_out(model, n)
    data_out_as_json = json.dumps(data_out)
    return data_out_as_json

@app.errorhandler(405)
def bad_method(error):
    return "Requests must be made via POST", 405

if __name__=="__main__":
    app.run(host='0.0.0.0')
