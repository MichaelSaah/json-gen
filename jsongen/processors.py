import random, copy, json
from .generators import Generate

generate = Generate()


def replace_values(d):
    if isinstance(d, list):
        return list(map(replace_values, d))
    elif isinstance(d, dict):
        return {k: replace_values(v) for k,v in d.items()}
    elif isinstance(d, str):
        return generate(d)
    else:
        return d


def calculate_cost(d):
    cost = 0
    def cc(d):
        nonlocal cost
        if isinstance(d, list):
            return list(map(cc, d))
        elif isinstance(d, dict):
            return {k: cc(v) for k,v in d.items()}
        elif isinstance(d, str):
            cost += generate.cost(d)
        else:
            return d
    cc(d)

    return cost


def build_data_out(model, n):
    """
    Returns n copies of the model with values subsituted from the database
    """

    data_out = []
    for _ in range(n):
        data_out.append(replace_values(copy.deepcopy(model)))

    return data_out
