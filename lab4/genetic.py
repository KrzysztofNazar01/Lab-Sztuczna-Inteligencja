import random

import numpy as np
from utils import fitness


class Genetic:
    def __init__(self, coords, population_size=100, elite_size=10, mutation_rate=0.01):
        self.coords = coords
        self.population_size = population_size
        self.elite_size = elite_size
        self.mutation_rate = mutation_rate

    def population_fitness(self, population):
        population_fitness = {}
        for i, individual in enumerate(population):
            # 1/fitness -> change to maximization problem
            population_fitness[i] = 1/fitness(self.coords, individual)

        return {k: v for k, v in sorted(population_fitness.items(), key=lambda item: item[1], reverse=True)}

    def best_solution(self, population):
        population_fitness = list(self.population_fitness(population))
        best_ind = population_fitness[0]
        return population[best_ind]

    def initial_population(self):
        population = []
        # Create initial population
        for i in range(self.population_size):
            solution = np.random.permutation(len(self.coords))
            population.append(solution)

        return population

    # get the best elements from the population
    # use roulette's method (Polish: metoda ruletki)
    def selection(self, population):
        result = []
        population_fitness = self.population_fitness(population)
        probability = dict()
        sum_fitness = sum(population_fitness.values())
        probability_previous = 0.0

        # fitting function
        for key, value in sorted(population_fitness.items()):
            probability[key] = probability_previous + value / sum_fitness
            probability_previous = probability[key]

        # save elite elements
        elite_count = 0
        for key in population_fitness.keys():
            if elite_count < self.elite_size:
                result.append(population[key])
                elite_count += 1
            else:
                break

        # save the rest of the elements
        for i in range(self.elite_size, len(population)):
            rand = random.random()
            for key, value in probability.items():
                if rand <= value:
                    result.append(population[key])
                    break

        return result

    def crossover_population(self, population):
        children = []

        # firstly save the elite elements
        for i in range(self.elite_size):
            children.append(population[i])

        # next get the rest of the elements
        for i in range(self.elite_size, len(population)):
            parents = random.sample(population, 2)

            # get slice (indexes) --> it will be moved to the second parent
            slice = np.random.randint(0, len(self.coords), 2)

            # switch the indexes if possible
            if slice[0] > slice[1]:
                slice[0], slice[1] = slice[1], slice[0]

            child = [None] * len(self.coords)

            for j in range(slice[0], slice[1] + 1):
                child[j] = parents[0][j]

            # create offspring basing on slice from the first parent and the data of the second parent
            offspring = [x for x in parents[1] if x not in child]

            offspring_ind = 0
            for j in range(len(child)):
                if child[j] is None:
                    child[j] = offspring[offspring_ind]
                    offspring_ind += 1

            children.append(child)

        return children

    def mutate_population(self, population): # swap two random elements

        for i in range(self.elite_size, len(population)):
            # get two random indexes
            index = np.random.randint(0, len(self.coords), 2)
            first = index[0]
            second = index[1]

            # swap
            population[i][first], population[i][second] = population[i][second], population[i][first]

        return population

    def next_generation(self, population):
        selection = self.selection(population)
        children = self.crossover_population(selection)
        next_generation = self.mutate_population(children)
        return next_generation
