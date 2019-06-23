import src.crossover as crossover
import src.utils as utils
from src.individual import Individual
from src.chromosome import generate_random_chromosome
from src.process_types import ProcessTypes


class GenGo:
    def __init__(self, chromosome_size=10, population_size=100, population_cutoff=0.5, iterations=100):
        self.chromosome_size = chromosome_size
        self.population_size = population_size
        self.population_cutoff = population_cutoff
        self.iterations = iterations
        self.current_generation = 0
        self.current_individuals = []

        self.initialize_callback = self.__default_initialize__
        self.process_callbacks = []  # two possible types of process callbacks
        self.fitness_callback = None
        self.select_generation_callback = self.__default_select_generation__
        self.select_parents_callback = self.__default_select_parents__
        self.crossover_callback = self.__default_crossover__
        self.terminate_callback = self.__default_terminate__

    def initialize(self, callback):
        self.initialize_callback = callback
        return self

    def process_individual(self, callback):
        self.process_callbacks.append((callback, ProcessTypes.INDIVIDUAL))
        return self

    def process_batch(self, callback):
        self.process_callbacks.append((callback, ProcessTypes.BATCH))
        return self

    def fitness(self, callback):
        self.fitness_callback = callback
        return self

    def select_generation(self, callback):
        self.select_generation_callback = callback
        return self

    def select_parents(self, callback):
        self.select_parents_callback = callback
        return self

    def cross_over(self, callback):
        self.crossover_callback = callback
        return self

    def terminate(self, callback):
        self.terminate_callback = callback
        return self

    def __default_initialize_callback(self):
        individuals = [Individual(generate_random_chromosome(self.chromosome_size))
                       for _ in range(self.population_size)]
        return individuals

    def __default_select_generation__(self, individuals):
        # assumes individuals have been sorted before call
        return individuals[: int(len(individuals)*self.population_cutoff)]

    def __default_select_parents__(self, individuals):
        return utils.random_two_elements(individuals)

    def __default_crossover__(self, individual_1, individual_2):
        return crossover.center_cross_over(individual_1.chromosome, individual_2.chromosome, self.chromosome_size)

    def __default_terminate__(self, individuals):
        return self.current_generation == self.iterations

    # TODO: function needs to be parallelize
    def parallelize_task_on_individuals(self, callback):
        for individual in self.current_individuals:
            callback(individual)

    @staticmethod
    def generate_fitness_sorted(individuals):
        return sorted(individuals, key=lambda individual: individual.fitness)

    def run(self):
        if not self.process_callback:
            raise Exception('Cannot run without processing function')

        if not self.fitness_callback:
            raise Exception('Cannot run without fitness function')

        self.initialize_callback()
        while not self.terminate_callback(self.current_individuals):
            # perform processing callbacks
            for process in self.process_callbacks:
                callback = process[0]
                process_type = process[1]
                if process_type is ProcessTypes.INDIVIDUAL:
                    self.parallelize_task_on_individuals(callback)
                else:
                    callback(self.current_individuals)

            # perform fitness callbacks
