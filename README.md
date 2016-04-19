# Genetic algorithm for the travelling salesman problem

## How it works. Take a look at genetic.py

First of all I should say that here we are considering such kind of
travelling salesman problem where cities to start and to finish
the salesman journey are given.

Step 1. All distances between cities are given in a matrix called
weights, so each diagonal cell equals 0 and ij-cell is
a distance between cities i and j.

Step 2. For making **initial population** we set its size ```pop_size```
and number of generations(```gen_max```)In method ```generate_population```
 we generate
initial population randomly.

Step 3. **Crossover.** We take two random parents(paths) and apply a
crossover method for them. ```crossover(self, mother, father)```
The number of taken chromosomes from mother and father are
generated randomly.

Step 4. **Mutation** Each child after crossover exposed to mutation.
in ``chromosome.py`` you can see method ```mutate``` which just swaps two
chromosomes in a gene. So yes 100% of population is mutated.

Step 5. **Fitness** We measure fitness of each generation by measuring
length of proposed path. In each iteration of algorithm work we are
looking for the fittest path and put into ```best``` variable.

Step 6. **Selection** Method ```selection``` sort new generation and
previous generation using fitness function and gives out the best
representatives of each generation and put it together updating
population array.

In a cycle we are repeating steps 3, 4, 5 and 6 for 1000 times.