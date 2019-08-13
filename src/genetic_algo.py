from typing import Callable, List, Tuple

import src.utils as utils
from enum import Enum
from src.individual import Individual
from src.chromosome import generate_random_chromosome
from src.selection import RouletteWheel
from src.crossover import SinglePointCross


class UserCallbackTypes(Enum):
    ITERATION_START = 0,
    AFTER_PROCESSING = 1,
    AFTER_FITNESS = 2,
    AFTER_ELITISM = 3,
    AFTER_MUTATION = 4,
    ITERATION_END = 5


class GenGo:
    """
    Genetic Algorithm. An evolutionary framework that allows user to optimize parameters of a problem.

    Attributes:
        chromosome_size: size of the chromosome in number of bits (bits to optimize)
        population_size: Fixed population size for each generation
        iterations: Number of iterations algorithm undergoes before termination. Overriden with user defined termination
        print_generation_info: Boolean to print information of each generation
        current_generation: The current generation number
        process_batch_size: Process function batch size to process at once
        current_individuals: Individuals in current generation

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
        self.process_batch_size = 1
        self.current_individuals = []

        self.initialize_callback = self.__default_initialize__
        self.process_callback = None
        self.fitness_callback = None
        self.select_parents_callback = RouletteWheel.select_parents
        self.crossover_callback = SinglePointCross.crossover
        self.mutate_callback = None  # TODO: Create default mutate callbacks
        self.terminate_callback = self.__default_terminate__
        self.user_defined_callbacks = dict((data, []) for data in UserCallbackTypes)

    def initialize(self, callback: Callable[['GenGo'], List[Individual]]):
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
        self.process_batch_size = batch_size
        if 1 <= batch_size <= self.population_size:
            self.process_callback = callback
        else:
            raise ValueError('Batch size must be between 1 and population size')
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

        :param callback: Function to call during parent selection step
        :return: self
        """
        self.select_parents_callback = callback
        return self

    def cross_over(self, callback: Callable[[Tuple[Individual, Individual]], Tuple[int, ...]]):
        """
        Cross over function to determine progeny from parents. This is part of the elitism step.

        :param callback: Function to call during cross over step
        :return: self
        """
        self.crossover_callback = callback
        return self

    # TODO: Create mutate algorithms
    def mutate(self, callback: Callable[[Individual], Individual]):
        """
        Mutation function to mutate individuals based on a mutation rate

        :param callback: Function to call during mutation step
        :return: self
        """
        self.mutate_callback = callback
        return self

    def terminate(self, callback: Callable[['GenGo'], bool]):
        """
        Terminate function to terminate stop of algorithm. Returns a boolean specifying state.

        :param callback: Function to call during terminate step
        :return: self
        """
        self.terminate_callback = callback
        return self

    def add_callback(self, callback: Callable[['GenGo'], None], callback_type: UserCallbackTypes):
        """
        User defined callbacks during iteration. Callback added to list of callbacks for specific location.
        Callbacks executed based on location [callback_type] and first added (Queue)

        :param callback: User defined function
        :param callback_type: Location of callback. See UserCallbackTypes
        :return: self
        """
        self.user_defined_callbacks[callback_type].append(callback)
        return self

    def __create_next_generation__(self):
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

    @staticmethod
    def __default_initialize__(algorithm):
        individuals = [Individual(algorithm.chromosome_size, generate_random_chromosome(algorithm.chromosome_size))
                       for _ in range(algorithm.population_size)]
        return individuals

    @staticmethod
    def __default_terminate__(algorithm):
        return algorithm.current_generation == algorithm.iterations

    def __print_generation_info__(self):
        print("Generation: ", self.current_generation)
        print("Max Fit Individual: ")
        max_fitness_individual = max(self.current_individuals, key=lambda individual: individual.fitness)
        print(max_fitness_individual)
        print("Min Fit Individual: ")
        min_fitness_individual = min(self.current_individuals, key=lambda individual: individual.fitness)
        print(min_fitness_individual)
        print("\n")

    def perform_user_defined_callback(self, callback_type:UserCallbackTypes):
        for callback in self.user_defined_callbacks[callback_type]:
            callback(self)

    def run(self):
        if not self.process_callback:
            raise Exception('Cannot run without processing function')

        if not self.fitness_callback:
            raise Exception('Cannot run without fitness function')

        # TODO: add exceptions if other functions are not initialized (should be defaulted by algorithm)

        # call initialization callback and reset population size
        self.current_individuals = self.initialize_callback(self)
        self.population_size = len(self.current_individuals)  # TODO: Automatically changes population size

        # initial generation print
        if self.print_generation_info:
            self.__print_generation_info__()

        while not self.terminate_callback(self):
            # perform user defined callbacks ITERATION_START
            self.perform_user_defined_callback(UserCallbackTypes.ITERATION_START)

            # perform process callback
            index = 0
            while index < self.population_size:
                self.process_callback(self.current_individuals[index : index + self.process_batch_size])
                index += self.process_batch_size

            # perform user defined callbacks AFTER_PROCESSING
            self.perform_user_defined_callback(UserCallbackTypes.AFTER_PROCESSING)

            # perform fitness callbacks
            for individual in self.current_individuals:
                individual.fitness = self.fitness_callback(individual)

            # perform user defined callbacks AFTER_FITNESS
            self.perform_user_defined_callback(UserCallbackTypes.AFTER_FITNESS)

            # print generation info
            if self.print_generation_info:
                self.__print_generation_info__()

            # perform parent selection and crossover part of elitism
            self.current_individuals = self.__create_next_generation__()

            # perform user defined callbacks AFTER_ELITISM
            self.perform_user_defined_callback(UserCallbackTypes.AFTER_ELITISM)

            # TODO: Mutation callbacks, user defined callback after mutation and iteration end

            # increment generation count
            self.current_generation += 1

