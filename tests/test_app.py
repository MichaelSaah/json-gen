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


def _holder_for_json_parsing_test():
    # case: working
    test_json = """
    {
    "model" : {"name" : {"first": "firstName", "last": "lastName"}},
    "n" : 10
    }
    """
    model, n = process_json(test_json.encode('utf-8'))

    correct_model = {"name" : {"first": "firstName", "last": "lastName"}}
    correct_n = 10

    assert model == correct_model
    assert n == correct_n

    # case: catch bad json
    test_json = """
    {
    "model" : {"name" : "first": "firstName", "last": "lastName"}},
    "n" : 10
    }
    """
    failed = False
    try:
        _, _ = process_json(test_json.encode('utf-8'))
    except Exception:
        failed = True
    assert failed

    # case: no n
    test_json = """
    {
    "model" : {"name" : {"first": "firstName", "last": "lastName"}}
    }
    """
    failed = False
    try:
        _, _ = process_json(test_json.encode('utf-8'))
    except Exception:
        failed = True
    assert failed

    # case: n not an int
    test_json = """
    {
    "model" : {"name" : {"first": "firstName", "last": "lastName"}},
    "n" : "not an int"
    }
    """
    failed = False
    try:
        _, _ = process_json(test_json.encode('utf-8'))
    except Exception:
        failed = True
    assert failed

    # case: n negative
    test_json = """
    {
    "model" : {"name" : {"first": "firstName", "last": "lastName"}},
    "n" : -10
    }
    """

    failed = False
    try:
        _, _ = process_json(test_json.encode('utf-8'))
    except Exception:
        failed = True
    assert failed

    # case: no model
    test_json = """
    {
    "n" : 10
    }
    """

    failed = False
    try:
        _, _ = process_json(test_json.encode('utf-8'))
    except Exception:
        failed = True
    assert failed


