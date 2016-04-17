import random
from chromosome import Chromosome

dim = 5
chromosome_length = dim - 2

weights = [
    [0,    5,   2,   100,  7],
    [5,    0,   3,    40,  4],
    [2,    3,   0,     6, 13],
    [100, 40,   6,     0, 12],
    [7,    4,  13,    12,  0]
]


class GeneNetwork(object):
    def __init__(self, dim, weights, chromosome_length, source, destination):
        self.chromosome_length = chromosome_length
        self.dim = dim
        self.weights = weights
        self.source = source
        self.destination = destination
        self.population = []
        self.population_size = 0

    def start(self, gen_max, pop_size):
        gen = 1  # from first generation
        self.generate_population(pop_size)  # generate initial population
        self.population_size = pop_size
        while gen <= gen_max:
            gen += 1
            p = 1
            while p <= self.population_size:
                p += 1
                parents = random.sample(range(self.population_size), 2)
                newbie = self.crossover(*parents)
                newbie.mutate()


    def generate_population(self, n):
        """

        :param n: number of chromosomes
        :return:
        """
        chromosomes = list()
        for i in range(n):
            chromosomes.append(self._gen_chromosome())
        self.population = chromosomes

    def _gen_chromosome(self):
        """

        :return: random path from source to destination
        """
        chromosome = random.sample(list(set(range(self.dim)) - {self.source, self.destination}),
                                   self.chromosome_length - 2)
        chromosome.insert(0, self.source)
        chromosome.append(self.destination)
        return Chromosome(chromosome)

    def crossover(self, mother, father):
        mother_list = mother.get()
        father_list = father.get()
        cut = random.randint(0, self.chromosome_length - 1)
        child = mother_list[0:cut] + father_list[cut + 1:]
        return Chromosome(child)




if __name__ == "__main__":
    gene_network = GeneNetwork(dim, weights, chromosome_length, 3, 7)
    gene_network.start(50, 10)