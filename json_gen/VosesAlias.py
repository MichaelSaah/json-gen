import random

class VosesAlias:
    """
    Vose's Alias is a variation of the alias algorithm for sampling
    from an arbitrary given discrete probability distribution. To use,
    simply pass a list of values (of any type) you'd like sampled, 
    and a list of weights specifying the probability of sampling each 
    value.

    Given the nature of floating-point comparison, we leave it up 
    to the user to make sure that the weights defines a 
    probability distribution; that is, that they sums to one. The 
    algorithm can handle some amount of numerical noise, so don't 
    sweat this too hard.
    """
    def __init__(self, values, weights):
        if len(values) != len(weights):
            raise ValueError('Values and weights lack parity. \
                Please pass the same number of values and weights.')

        self.values = values
        self.n = len(weights)

        scaled_weights = list(map(lambda x: x*self.n, weights))
        small = []
        large = []

        alias = [0]*self.n
        prob = [0]*self.n

        for i,p in enumerate(scaled_weights):
            if p < 1:
                small.append(i)
            else:
                large.append(i)

        while large and small:
            l = small.pop(0)
            g = large.pop(0)
            prob[l] = scaled_weights[l]
            alias[l] = g
            scaled_weights[g] = scaled_weights[g] + scaled_weights[l] - 1
            if scaled_weights[g] < 1:
                small.append(g)
            else:
                large.append(g)

        while large:
            g = large.pop(0)
            prob[g] = 1
       
        while small: # large should be exhausted first, 
                     # this catches numerical error
            l = small.pop(0)
            prob[l] = 1

        self.alias = alias
        self.prob = prob

    def __call__(self):
        i = random.sample(range(self.n), 1)[0]
        if random.random() < self.prob[i]:
            return self.values[i]
        else:
            return self.values[self.alias[i]]
