import random
import copy
import json
from .database import database as db


def replace_values(d):
    if isinstance(d, list):
        return list(map(replace_values, d))
    elif isinstance(d, dict):
        return {k: replace_values(v) for k,v in d.items()}
    elif isinstance(d, str):
        if d in db:
            return random.sample(db[d],1)[0]
        else:
            return None
    else:
        return None


def process_json(json_str):
    """
    On success: Returns the tuple (model, n), where model is the
    data template dict and n is the number of copies requested
    On failure: Raises an exception
    """
    data = json.loads(json_str)

    if "n" in data:
        n = data["n"]
    else:
        raise Exception("No value found for n")

    if not isinstance(n, int):
        raise Exception("n must be a positive integer")

    if n < 1:
        raise Exception("n must be a positive integer")

    if "model" in data:
        model = data["model"]
    else:
        raise Exceptions("No value found for model")

    return model, n


def build_data_out(model, n):
    data_out = []
    for _ in range(n):
        data_out.append(replace_values(copy.deepcopy(model)))

    return data_out
