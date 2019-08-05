from typing import Callable, List, Tuple

import src.crossover as crossover
import src.utils as utils
from src.gengo_types import ProcessTypes, UserCallbackTypes
from src.individual import Individual
from src.chromosome import generate_random_chromosome
from src.selection import RouletteWheel


class GenGo:
    """
    Genetic Algorithm. User specifies values to optimize and the algorithms undergoes steps of
    evolutionary algorithm

    Attributes:
        chromosome_size: size of the chromosome in number of bits (bits to optimize)
        population_size: Fixed population size for each generation
        iterations: Number of iterations algorithm undergoes before termination. Overriden with user defined termination
        print_generation_info: boolean to print information of each generation
        current_generation: The current generation number

        initialize_callback: function called once during the start of the genetic algorithm
        process_callback: function to process generation called every iteration. User defined function is mandatory.
        fitness_callback: function called after process function. User defined function is mandatory.
        select_parents_callback: function to choose parents to mate
        crossover_callback: function to cross parents to produce offspring
        terminate_callback: function to terminate evolutionary algorithm
        user_defined_callbacks: dictionary of callbacks that users can add other than normal functions in GenGo
    """

    def __init__(self, chromosome_size=10, population_size=100, iterations=100,
                 print_generation_info=True):
        self.chromosome_size = chromosome_size
        self.population_size = population_size
        self.iterations = iterations
        self.print_generation_info = print_generation_info
        self.current_generation = 0
        self.current_individuals = []

        self.initialize_callback = self.__default_initialize__
        self.process_callback = None
        self.fitness_callback = None
        self.select_parents_callback = RouletteWheel.select_parents
        self.crossover_callback = self.__default_crossover__
        self.mutate_callback = None  # TODO: Create default mutate callbacks
        self.terminate_callback = self.__default_terminate__
        self.user_defined_callbacks = dict((i, []) for i in range(0, UserCallbackTypes.ITERATION_END + 1))

    def initialize(self, callback: Callable[[None], List[Individual]]):
        """
        Initialize function called at start of the genetic algorithm.
        Defaulted to creating list[population_size] of random individuals.

        :param callback: Function to call during initialization step
        :return: self
        """
        self.initialize_callback = callback
        return self

    def process(self, callback: Callable[[List[Individual]], None], batch_size=1):
        """
        Process function called every iteration of algorithm to process individuals.
        Mandatory function needs to be passed in.
        User can specify batch processing or individual processing. Throws error if batch size is invalid

        :param callback: Function to call during processing step
        :param batch_size: Number of individuals to process at same time
        :return: self
        """
        if batch_size == 1:
            self.process_callback = (callback, ProcessTypes.INDIVIDUAL)
        elif 1 < batch_size <= self.population_size:
            self.process_callback = (callback, ProcessTypes.BATCH)
        else:
            pass  # TODO: Throw error if batch size is not within limits
        return self

    def fitness(self, callback: Callable[[Individual], float]):
        """
        Fitness function called after processing individuals.
        Mandatory function needs to be passed in.

        :param callback: Function to call during fitness step
        :return: self
        """
        self.fitness_callback = callback
        return self

    def select_parents(self, callback: Callable[[List[Individual]], Tuple[Individual, Individual]]):
        """
        Select parents function to determine ancestors of next generation. This is part of the elitism step.
        TODO: Function is defaulted to Roulette Wheel Selection

        :param callback: Function to call during parent selection step
        :return: self
        """
        self.select_parents_callback = callback
        return self

    def cross_over(self, callback: Callable[[Tuple[Individual, Individual]], Tuple[...]]):
        """
        Cross over function to determine progeny from parents. This is part of the elitism step.
        TODO: Function is defaulted to single point cross over

        :param callback: Function to call during cross over steo
        :return: self
        """
        self.crossover_callback = callback
        return self

    # TODO: Create mutate algorithms
    def mutate(self, callback: Callable[[Individual], Individual]):
        self.mutate_callback = callback
        return self

    # TODO: Terminate callback will get reference to self as parameter (Add Typing)
    def terminate(self, callback):
        self.terminate_callback = callback
        return self

    # TODO: Callbacks will get reference to self as parameter (Add Typing)
    def add_callback(self, callback, callback_type):
        self.user_defined_callbacks[callback_type].append(callback)
        return self

    def __default_initialize__(self):
        individuals = [Individual(self.chromosome_size, generate_random_chromosome(self.chromosome_size))
                       for _ in range(self.population_size)]
        return individuals

    def __default_crossover__(self, individual_1, individual_2):
        return crossover.center_cross_over(individual_1.chromosome, individual_2.chromosome, self.chromosome_size)

    def __default_terminate__(self, individuals):
        return self.current_generation == self.iterations

    def __run_process_callback__(self):
        process_type = self.process_callback[1]
        process_callback = self.process_callback[0]
        if process_type == ProcessTypes.INDIVIDUAL:
            for individual in self.current_individuals:
                process_callback(individual)
        else:
            process_callback(self.current_individuals)

    def __run_fitness_callback__(self):
        for individual in self.current_individuals:
            individual.fitness = self.fitness_callback(individual)

    def __run_create_next_generation__(self):
        next_generation = []
        while len(next_generation) != self.population_size:
            parents = self.select_parents_callback(self.current_individuals)
            if len(parents) != 2:
                raise Exception('Parent selection must return two individuals')
            chromosomes = self.crossover_callback(*parents)
            current_index = 0
            while current_index < len(chromosomes) and len(next_generation) != self.population_size:
                chromosome = chromosomes[current_index]
                if not 0 <= chromosome <= utils.max_binary_value(self.chromosome_size):
                    raise Exception('Chromosomes generated must be between within max chromosome value')
                individual = Individual(self.chromosome_size, chromosome)
                individual.set_parents(*parents)
                next_generation.append(individual)
                current_index += 1
        return next_generation

    def __print_generation_info__(self):
        print("Generation: ", self.current_generation)
        print("Max Fit Individual: ")
        print(self.max_fitness_individual(self.current_individuals))
        print("Min Fit Individual: ")
        print(self.min_fitness_individual(self.current_individuals))
        print("\n")

    @staticmethod
    def generate_fitness_sorted(individuals):
        return sorted(individuals, key=lambda individual: individual.fitness)

    @staticmethod
    def max_fitness_individual(individuals):
        return max(individuals, key=lambda individual: individual.fitness)

    @staticmethod
    def min_fitness_individual(individuals):
        return min(individuals, key=lambda individual: individual.fitness)

    def run(self):
        if not self.process_callback:
            raise Exception('Cannot run without processing function')

        if not self.fitness_callback:
            raise Exception('Cannot run without fitness function')

        # call initialization callback and reset population size
        self.current_individuals = self.initialize_callback()
        self.population_size = len(self.current_individuals)

        # initial generation print
        if self.print_generation_info:
            self.__print_generation_info__()

        while not self.terminate_callback(self.current_individuals):
            # perform process callback
            self.__run_process_callback__()

            # perform fitness callbacks
            self.__run_fitness_callback__()

            # print generation info
            if self.print_generation_info:
                self.__print_generation_info__()

            # perform generation selection
            self.current_individuals = self.select_generation_callback(self.current_individuals)

            # perform parent selection and crossover
            self.current_individuals = self.__run_create_next_generation__()

            # increment generation count
            self.current_generation += 1
