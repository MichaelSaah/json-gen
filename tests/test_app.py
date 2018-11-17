import os, tempfile, pytest, json
from app import app, db, models
from flask_migrate import upgrade
from flask import jsonify

@pytest.fixture
def client():
    db_fd, path = tempfile.mkstemp()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path
    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        db.init_app(app)
        upgrade()

    test_user = models.User(username='Mike')
    db.session.add(test_user)
    db.session.commit()
    
    yield client

    os.close(db_fd)
    os.unlink(path)

endpoint = '/api/'

def test_api_view(client):
    test_data = {
    "model" : {"name" : {"first": "firstName", "last": "lastName"}},
    "n" : 10,
    "user" : "Mike",
    }
    res = client.post(endpoint, data=json.dumps(test_data))
    assert res.status_code == 200
    

def _holder_for_json_parsing_test():
    # case: working
    
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


