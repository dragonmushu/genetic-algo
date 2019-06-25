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
        self.process_callback = None
        self.fitness_callback = None
        self.select_generation_callback = self.__default_select_generation__
        self.select_parents_callback = self.__default_select_parents__
        self.crossover_callback = self.__default_crossover__
        self.terminate_callback = self.__default_terminate__

    def initialize(self, callback):
        self.initialize_callback = callback
        return self

    def process_individual(self, callback):
        self.process_callback = (callback, ProcessTypes.INDIVIDUAL)
        return self

    def process_batch(self, callback):
        self.process_callback = (callback, ProcessTypes.BATCH)
        return self

    def process_batch(self, callback, n):
        pass

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

    def __run_process_callback__(self):
        process_type = self.process_callback[1]
        process_callback = self.process_callback
        if process_type == ProcessTypes.INDIVIDUAL:
            for individual in self.current_individuals:
                process_callback(individual)
        else:
            process_callback(self.current_individuals)

    def __run_fitness_callback__(self):
        for individual in self.current_individuals:
            individual.fitness = self.fitness_callback(individual)

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
            # perform process callback
            self.__run_process_callback__()

            # perform fitness callbacks
            self.__run_fitness_callback__()

            # sort generation based on fitness value
            self.current_individuals = self.generate_fitness_sorted(self.current_individuals)

            # perform generation selection
            self.current_individuals = self.select_generation_callback(self.current_individuals)

            # perform parent selection and crossover
