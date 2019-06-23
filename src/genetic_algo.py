import src.crossover as crossover
import src.utils as utils


class GenGo:
    def __init__(self, chromosome_size=10, population_size=100, population_cutoff=0.5, iterations=100):
        self.chromosome_size = chromosome_size
        self.population_size = population_size
        self.population_cutoff = population_cutoff
        self.iterations = iterations
        self.current_generation = 0

        self.process_callbacks = []  # two possible types of process callbacks
        self.fitness_callback = None
        self.select_generation_callback = self.__default_select_generation__
        self.select_parents_callback = self.__default_select_parents__
        self.crossover_callback = self.__default_crossover__
        self.terminate_callback = self.__default_terminate__

    def process_individual(self, callback):
        self.process_callbacks.append(callback)
        return self

    def process_batch(self, callback):
        self.process_callbacks.append(callback)
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

    def __default_select_generation__(self, individuals):
        # assumes individuals have been sorted before call
        return individuals[: int(len(individuals)*self.population_cutoff)]

    def __default_select_parents__(self, individuals):
        return utils.random_two_elements(individuals)

    def __default_crossover__(self, individual_1, individual_2):
        return crossover.center_cross_over(individual_1.chromosome, individual_2.chromosome, self.chromosome_size)

    def __default_terminate__(self, individuals):
        return self.current_generation == self.iterations

    @staticmethod
    def generate_fitness_sorted(individuals):
        return sorted(individuals, key=lambda individual: individual.fitness)

    def run(self):
        if not self.process_callback:
            raise Exception('Cannot run without processing function')

        if not self.fitness_callback:
            raise Exception('Cannot run without fitness function')








