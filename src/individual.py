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

    def add_metric(self, key, val, average=False):
        if key not in self.metrics or not average:
            self.metrics[key] = (val, 1)
        else:
            metric = self.metrics[key]
            old_avg = metric[0]
            old_size = metric[1]
            avg = (old_avg * old_size + val)/(old_size + 1)
            self.metrics[key] = (avg, old_size + 1)

    def get_metric(self, key):
        return self.metrics[key][0]

    def gene_active(self, position):
        return utils.bit_set(self.chromosome, position)

    def clear_metrics(self):
        self.metrics = {}

