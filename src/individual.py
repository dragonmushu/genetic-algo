import src.utils as utils


class Individual:
    def __init__(self, chromosome=0):
        self.parent1 = None
        self.parent2 = None
        self.chromosome = chromosome
        self.fitness = 0
        self.metrics = {}

    def set_parents(self, p1, p2):
        self.parent1 = p1
        self.parent2 = p2

    def add_metric(self, key, val):
        self.metrics[key] = val

    def get_metric(self, key):
        return self.metrics[key]

    def gene_active(self, position):
        return utils.bit_set(self.chromosome, position)

    def __clear_metrics__(self):
        self.metrics = {}

