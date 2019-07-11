import src.utils as utils
from src.chromosome import chromosome_subset_value


class Individual:
    def __init__(self, chromosome_size, chromosome=0):
        self.parent1 = None
        self.parent2 = None
        self.chromosome_size = chromosome_size
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
        if not 1 <= position <= self.chromosome_size:
            raise ValueError()
        return utils.bit_set(self.chromosome, position)

    def gene_value(self, start_position, end_position):
        if not 1 <= start_position <= end_position <= self.chromosome_size:
            raise ValueError()
        return chromosome_subset_value(self.chromosome, start_position, end_position - start_position + 1)

    def clear_metrics(self):
        self.metrics = {}

    def __str__(self):
        score = "Fitness Score: " + str(self.fitness) + "\n"
        chromosome = "Chromosome: " + str(self.chromosome) + "\n"
        parent1 = ""
        parent2 = ""
        if self.parent1 and self.parent2:
            parent1 = "Parent 1 Chromosomes: " + str(self.parent1.chromosome) + "\n"
            parent2 = "Parent 2 Chromosome: " + str(self.parent2.chromosome) + "\n"
        return score + chromosome + parent1 + parent2
