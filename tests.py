from jsongen.processors import replace_values, process_json
from jsongen.generators import Generate
from jsongen.utilities import WeightedSampler
import string

db = Generate()


def test_generators():
    # case: general sampler test
    t = db('_tester')
    assert t in db._db['_tester'].values

    # case: WeightedSampler
    wb = WeightedSampler(['a', 'b', 'c'], [0.4, 0.6, 0])
    for _ in range(100):
        assert wb() in ['a', 'b']

    # case: not found:
    nf = db('not found, leave me be')
    assert nf == 'not found, leave me be'

    # case: array
    values = db('array|5|_tester')
    for v in values:
        assert v in db._db['_tester'].values

    # case: array with bad n
    bad_args = ['array|2.3|_tester', 'array|-3|_tester', 'array|n|_tester']
    for a in bad_args:
        assert a == db(a)

    # case: eMail
    em = db('eMail')
    usr, dom = em.split('@')
    assert usr.isalnum()
    subd, tld = dom.split('.')
    assert subd
    assert tld

    # case: time_formatter
    # TODO

    # case: numberInt - this case covers IntegerBetween
    nums = db('array|100|numberInt|-100|100')
    for n in nums:
        assert -100 <= n <= 100

    # case: numberFloat - this case covers FloatBetween
    nums = db('array|100|numberFloat|-100|100|3')
    for n in nums:
        assert -100 <= n <= 100
        assert len(str(n).split('.')[1]) <= 3

    # case: randomString - this case covers RandomChar
    assert 10 <= len(db('randomString')) <= 100
    assert len(db('randomString|10')) == 10
    chars = string.ascii_letters + string.digits
    for c in db('randomString'):
        assert c in chars

    # case: zipCode
    for _ in range(1000):
        zc = db('zipCode')
        assert 0 <= int(zc) <= 99999
        assert len(zc) == 5

def test_replace_values():
    # case: general
    test_dict = {
        "name" : {"first": "_tester", "last": "_tester"},
        "age" : "_tester",
        "children" : ["_tester", "_tester", "_tester" ]
    }

    test_dict = replace_values(test_dict)
    assert test_dict["name"]["first"] in db._db["_tester"].values
    assert test_dict["name"]["last"] in db._db["_tester"].values
    assert test_dict["age"] in db._db["_tester"].values
    for f in test_dict["children"]:
        assert f in db._db["_tester"].values

    # case: nested lists
    test_dict = {
        "people" : [["_tester", "_tester"], ["_tester", "_tester"]]
    }

    test_dict = replace_values(test_dict)
    for f,l in test_dict["people"]:
        assert f in db._db["_tester"].values
        assert l in db._db["_tester"].values

    # case: non-(string,list,dict) values
    test_dict = {
        "int" : 3, "float" : 2.07, "bool" : True, "null" : None
    }
    test_dict = replace_values(test_dict)
    assert test_dict['int'] == 3
    assert test_dict['float'] == 2.07
    assert test_dict['bool'] == True
    assert test_dict['null'] == None

    # case: list
    test_list = ["_tester", "_tester"]
    test_list = replace_values(test_list)
    assert test_list[0] in db._db["_tester"].values
    assert test_list[1] in db._db["_tester"].values

    # case: naked value
    test_val = "_tester"
    test_val = replace_values(test_val)
    assert test_val in db._db["_tester"].values


def test_process_json():
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


if __name__ == "__main__":
    test_replace_values()
    test_generators()
    test_process_json()
