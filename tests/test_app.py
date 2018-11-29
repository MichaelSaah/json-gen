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

    # add test user to test db
    test_user = models.User(username='Mike')
    db.session.add(test_user)
    db.session.commit()
    
    yield client

    os.close(db_fd)
    os.unlink(path)


route = '/api/'

def test_api_view(client):
    # case: working, n given
    test_data = {
    "model" : {"name" : {"first": "firstName", "last": "lastName"}},
    "n" : 10,
    "user" : "Mike",
    }
    res = client.post(route, data=json.dumps(test_data))
    assert res.status_code == 200

    # case: working, no n given
    test_data = {
    "model" : {"name" : {"first": "firstName", "last": "lastName"}},
    "user" : "Mike",
    }
    res = client.post(route, data=json.dumps(test_data))
    assert res.status_code == 200

    # case: bad json
    res = client.post(route, data='{"Hi": "There"}}'.encode('utf-8'))
    assert res.status_code == 400
    
    # case: no model
    test_data = {
    "n": 10,
    "user" : "Mike",
    }
    res = client.post(route, data=json.dumps(test_data))
    assert res.status_code == 400

    # case: no user
    test_data = {
    "model" : {"name" : {"first": "firstName", "last": "lastName"}},
    "n": 10,
    }
    res = client.post(route, data=json.dumps(test_data))
    assert res.status_code == 400

    # case: n negative
    test_data = {
    "model" : {"name" : {"first": "firstName", "last": "lastName"}},
    "n" : -10,
    "user" : "Mike",
    }
    res = client.post(route, data=json.dumps(test_data))
    assert res.status_code == 400

    # case: n cannot be converted
    test_data = {
    "model" : {"name" : {"first": "firstName", "last": "lastName"}},
    "n" : "3.14",
    "user" : "Mike",
    }
    res = client.post(route, data=json.dumps(test_data))
    assert res.status_code == 400
