import random

import src.utils as utils


class GeneticAlgorithm:
    def __init__(self, chromosome_size = 10, population_size = 100, population_cutoff = 0.5, iterations = 100, fitness_termination = 0):
        self.chromosome_size = chromosome_size
        self.population_size = population_size
        self.population_cutoff = population_cutoff
        self.iterations = iterations
        self.fitness_termination = fitness_termination
        self.current_generation = 0

        self.process_callbacks = []
        self.fitness_callback = None
        self.crossover_callback = center_cross_over
        self.terminate_callback = None

    def process_individual(self, callback):
        self.process_callbacks.append(callback)
        return self

    def process_batch(self, callback):
        self.process_callbacks.append(callback)
        return self

    def fitness(self, callback):
        self.fitness_callback = callback
        return self

    def cross_over(self, callback):
        self.crossover_callback = callback
        return self

    def terminate(self, callback):
        self.terminate_callback = callback
        return self

    def run(self):
        if not self.process_callback:
            raise Exception('Cannot run without processing function')

        if not self.fitness_callback:
            raise Exception('Cannot run without processing function')

        if self.terminate_callback is None:
            for i in range(0, self.iterations):
                pass


def point_cross_over(chromosome_1, chromosome_2, size, point):
    mask = utils.max_binary_value(size) >> point
    offspring_1 = (chromosome_2 & mask) | (chromosome_1 & ~mask)
    offspring_2 = (chromosome_1 & mask) | (chromosome_2 & ~mask)
    return offspring_1, offspring_2


def center_cross_over(chromosome_1, chromosome_2, size):
    center = int(size/2)
    return point_cross_over(chromosome_1, chromosome_2, size, center)


def random_point_cross_over(chromosome_1, chromosome_2, size):
    point = random.randint(1, size)
    return point_cross_over(chromosome_1, chromosome_2, size, point)

def cutoff_termination





