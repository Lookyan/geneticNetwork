import random


class Chromosome(object):
    def __init__(self, vector):
        self.vector = vector

    def __repr__(self):
        return str(self.vector)

    def get(self):
        return self.vector

    def size(self):
        return len(self.vector)

    def path(self):
        # TODO: by weights
        return sum(self.vector)

    def mutate(self):
        pos = random.randint(1, self.size() - 2)
        self.vector[pos] = random.randint(0, self.size() - 1)