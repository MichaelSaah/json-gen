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
    test_user = models.User(username='Mike',
                            key='euSHRzqtK4EcPL1iNZ9CzA==')
    db.session.add(test_user)
    db.session.commit()
    
    yield client

    os.close(db_fd)
    os.unlink(path)


route = '/api/'
key='euSHRzqtK4EcPL1iNZ9CzA=='


def test_main_view(client):
    # case: working, n given
    test_data = {
    "model" : {"name" : {"first": "firstName", "last": "lastName"}},
    "n" : 10,
    "key" : "euSHRzqtK4EcPL1iNZ9CzA==",
    }
    res = client.post(route, data=json.dumps(test_data))
    assert res.status_code == 200

    # case: working, no n given
    test_data = {
    "model" : {"name" : {"first": "firstName", "last": "lastName"}},
    "key" : "euSHRzqtK4EcPL1iNZ9CzA==",
    }
    res = client.post(route, data=json.dumps(test_data))
    assert res.status_code == 200

    # case: bad json
    res = client.post(route, data='{"Hi": "There"}}'.encode('utf-8'))
    assert res.status_code == 400
    
    # case: no model
    test_data = {
    "n": 10,
    "key" : "euSHRzqtK4EcPL1iNZ9CzA==",
    }
    res = client.post(route, data=json.dumps(test_data))
    assert res.status_code == 400

    # case: no user
    test_data = {
    "model" : {"name" : {"first": "firstName", "last": "lastName"}},
    "n": 10,
    }
    res = client.post(route, data=json.dumps(test_data))
    assert res.status_code == 401

    # case: n negative
    test_data = {
    "model" : {"name" : {"first": "firstName", "last": "lastName"}},
    "n" : -10,
    "key" : "euSHRzqtK4EcPL1iNZ9CzA==",
    }
    res = client.post(route, data=json.dumps(test_data))
    assert res.status_code == 400

    # case: n cannot be converted
    test_data = {
    "model" : {"name" : {"first": "firstName", "last": "lastName"}},
    "n" : "3.14",
    "key" : "euSHRzqtK4EcPL1iNZ9CzA==",
    }
    res = client.post(route, data=json.dumps(test_data))
    assert res.status_code == 400

    # case: bad refresh
    test_data = {
    "model" : {"name" : {"first": "firstName", "last": "lastName"}},
    "key" : "euSHRzqtK4EcPL1iNZ9CzA==",
    "refresh" : "not a bool"
    }
    res = client.post(route, data=json.dumps(test_data))
    assert res.status_code == 400

def test_main_view_response_cacheing(client):
    # case: working, False refresh
    test_data = {
    "model" : {"name" : {"first": "firstName", "last": "lastName"}},
    "n" : 10,
    "key" : "euSHRzqtK4EcPL1iNZ9CzA==",
    "refresh": False
    }
    res_1 = client.post(route, data=json.dumps(test_data))
    res_2 = client.post(route, data=json.dumps(test_data))
    assert res_1.status_code == 200
    assert res_2.status_code == 200
    assert res_1.data == res_2.data

    # case: working, True refresh
    test_data = {
    "model" : {"name" : {"first": "firstName", "last": "lastName"}},
    "n" : 10,
    "key" : "euSHRzqtK4EcPL1iNZ9CzA==",
    "refresh": True
    }
    res_1 = client.post(route, data=json.dumps(test_data))
    res_2 = client.post(route, data=json.dumps(test_data))
    assert res_1.status_code == 200
    assert res_2.status_code == 200
    assert res_1.data != res_2.data


