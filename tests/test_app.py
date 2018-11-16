import requests, json

host = 'http://localhost:5000/api/'

def test_api_handler():
#TODO: reimplement process_json test in here
    # good request
    # todo: assert transaction processed properly
    data = {'user': 'Mike', 'n': 1, 'model': {'name': '_tester'}}
    r = requests.post(host, data=json.dumps(data))
    print(r.text)
    assert r.status_code == 200
