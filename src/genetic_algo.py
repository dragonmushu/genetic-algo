import src.crossover as crossover


class GenGo:
    def __init__(self, chromosome_size=10, population_size=100, population_cutoff=0.5, iterations=100,
                 fitness_termination=0):
        self.chromosome_size = chromosome_size
        self.population_size = population_size
        self.population_cutoff = population_cutoff
        self.iterations = iterations
        self.fitness_termination = fitness_termination
        self.current_generation = 0

        self.process_callbacks = []
        self.fitness_callback = None
        self.crossover_callback = crossover.center_cross_over
        self.select_generation_callback = self.__default_select_generation__
        self.select_parents_callback = self.__default_select_parents__
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

    def cross_over(self, callback):
        self.crossover_callback = callback
        return self

    def select_generation(self, callback):
        self.select_generation_callback = callback
        return self

    def select_parents(self, callback):
        self.select_parents_callback = callback
        return self

    def terminate(self, callback):
        self.terminate_callback = callback
        return self

    def __default_terminate__(self, individuals):
        pass

    def __default_select_generation__(self, individuals):
        pass

    def __default_select_parents__(self, individuals):
        pass

    def run(self):
        if not self.process_callback:
            raise Exception('Cannot run without processing function')

        if not self.fitness_callback:
            raise Exception('Cannot run without fitness function')








