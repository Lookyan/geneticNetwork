import random
from chromosome import Chromosome

dim = 5
chromosome_length = dim  # min is (dim - 2)

weights = [
    [0,    5,   2,   100,  7],
    [5,    0,   3,    40,  4],
    [2,    3,   0,     6, 13],
    [100, 40,   6,     0, 12],
    [7,    4,  13,    12,  0]
]

quite = False


class GeneNetwork(object):
    def __init__(self, dim, weights, chromosome_length, source, destination):
        """

        :param dim: problem dimension
        :param weights:
        :param chromosome_length: length of chromosome
        :param source: source node
        :param destination: destination node
        :return:
        """
        if source >= dim - 1 or destination >= dim - 1:
            raise ValueError
        self.chromosome_length = chromosome_length
        self.dim = dim
        self.weights = weights
        self.source = source
        self.destination = destination
        self.population = []
        self.population_size = 0

    def start(self, gen_max, pop_size):
        """

        :param gen_max: maximum number of generations
        :param pop_size: initial population size
        :return:
        """
        gen = 1  # from first generation
        self.generate_population(pop_size)  # generate initial population
        self.population_size = pop_size
        while gen <= gen_max:
            gen += 1
            p = 1
            while p <= self.population_size:
                p += 1
                parents = random.sample(range(self.population_size), 2)
                newbie = self.crossover(self.population[parents[0]], self.population[parents[1]])
                newbie.mutate()
                fit = self.fitness(newbie)
                pass


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
        """

        :param mother: first parent
        :param father: second parent
        :return: crossing over child
        """
        mother_list = mother.get()
        father_list = father.get()
        cut = random.randint(0, self.chromosome_length - 1)
        child = mother_list[0:cut] + father_list[cut:]
        return Chromosome(child)

    def fitness(self, chromosome):
        chromosome_list = chromosome.get()
        return sum([self.weights[i][j] for i, j in zip(chromosome_list[:-1], chromosome_list[1:])])


if __name__ == "__main__":
    gene_network = GeneNetwork(dim, weights, chromosome_length, 3, 1)
    gene_network.start(50, 10)  # start with 50 generations and 10 initial chromosomes