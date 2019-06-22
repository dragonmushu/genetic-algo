class GeneticAlgorithm:
    def __init__(self, chromosome_size = 10, population_size = 100, iterations = 100, population_selection = 0.5):
        self.chromosome_size = 10
        self.population_size = 100
        self.iterations = 100
        self.population_selection = population_selection
        self.process_callbacks = []
        self.fitness_callback = None
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

    def terminate_function(self, callback):
        self.terminate_callback = callback
        return self

    def run(self):
        if not self.process_callback or self.fitness_callback is None:


        if self.terminate_callback is None:
            for i in range(0, self.iterations):
                pass



algo = GeneticAlgorithm()

algo.process_individual().fitness_function().terminate_function().run()



