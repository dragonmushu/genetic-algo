class Individual:

    def __init__(self, chromosome_size=10):
        self.parent1 = None
        self.parent2 = None
        self.chromosome_size = chromosome_size
        self.chromosome = 0
        self.fitness = 0
        self.metrics = {}

    def set_parents(self, p1, p2):
        self.parent1 = p1
        self.parent2 = p2

    def add_metric(self, key, val):
        self.metrics[key] = val

    def get_metric(self, key, val):
        pass

    def gene_active(self, position):
        temp = 1 << (position - 1)
        return temp & self.chromosome != 0

    def __clear_metrics__(self):
        self.metrics = {}

