import random, string
from .VosesAlias import VosesAlias

# Building blocks for generators - not exposed to API

class Sampler:
    def __init__(self, values=None):
        if values:
            self.values = values
    def __call__(self):
        return random.sample(self.values, 1)[0]


class WeightedSampler(VosesAlias):
    pass
        

class IntegerBetween:
    @staticmethod
    def __call__(l, u):
        if l > u:
            raise ValueError('The lower bound must be less than or equal to the upper bound')
        return random.sample(range(l, u+1), 1)[0]


class FloatBetween:
    @staticmethod
    def __call__(l, u, k=None):
        width = u - l
        f =  random.random() * width + l
        if k:
            return round(f, k)
        else:
            return f


class RandomChar(Sampler):
    values = string.ascii_letters + string.digits

