from json_gen.gen import replace_values, process_json
from json_gen.database import database

def test_replace_values():
    # case: general
    test_dict = {
        "name" : {"first": "firstName", "last": "lastName"},
        "age" : "personAge",
        "children" : ["firstName", "firstName", "firstName" ]
    }

    test_dict = replace_values(test_dict)
    print(test_dict)
    assert test_dict["name"]["first"] in database["firstName"]
    assert test_dict["name"]["last"] in database["lastName"]
    assert test_dict["age"] in database["personAge"]
    for fname in test_dict["children"]:
        assert fname in database["firstName"]

    # case: nested lists
    test_dict = {
        "people" : [["firstName", "lastName"], ["firstName", "lastName"]]
    }

    test_dict = replace_values(test_dict)
    for f,l in test_dict["people"]:
        assert f in database["firstName"]
        assert l in database["lastName"]

    # case: non-(string,list,dict) values
    test_dict = {
        "int" : 3, "float" : 2.07, "bool" : True, "null" : None
    }
    test_dict = replace_values(test_dict)
    for _, v in test_dict.items():
        assert v is None

def test_process_json():
    # case: working
    test_json = """
    {
    "model" : {"name" : {"first": "firstName", "last": "lastName"}},
    "n" : 10
    }
    """
    model, n = process_json(test_json)

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
        _, _ = process_json(test_json)
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
        _, _ = process_json(test_json)
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
        _, _ = process_json(test_json)
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
        _, _ = process_json(test_json)
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
        _, _ = process_json(test_json)
    except Exception:
        failed = True
    assert failed


if __name__ == "__main__":
    test_replace_values()
