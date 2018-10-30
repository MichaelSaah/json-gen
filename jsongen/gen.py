import random, copy, json
from .database import database

db = database()


def replace_values(d):
    """
    Takes an object composed of elements of {dict, list, str} and recursively traverses
    it, replacing tags with values sampled from the database.
    If values are found that either are not strings or are not valid tags, None is inserted
    """

    if isinstance(d, list):
        return list(map(replace_values, d))
    elif isinstance(d, dict):
        return {k: replace_values(v) for k,v in d.items()}
    elif isinstance(d, str):
        return db(d)
    else:
        return d


def process_json(raw):
    """
    Returns the tuple (model, n), where model is the
    data template dict and n is the number of copies requested
    Will throw exceptions on the following conditions:
        n not present
        n not a positive integer
        model not present
    """

    data = json.loads(raw.decode('utf-8'))

    if "n" in data:
        n = data["n"]
    else:
        raise KeyError("n")

    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")

    if "model" in data:
        model = data["model"]
    else:
        raise KeyError("model")

    return model, n


def build_data_out(model, n):
    """
    Returns n copies of the model with values subsituted from the database
    """

    data_out = []
    for _ in range(n):
        data_out.append(replace_values(copy.deepcopy(model)))

    return data_out
