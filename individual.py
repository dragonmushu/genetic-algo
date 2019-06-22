#import random

class Individual:
    def __init__(self, chromosome_size = 10):
        self.parent1 = None
        self.parent2 = None
        self.chromosome_size = chromosome_size
        self.metrics = {}

    def set_parents(self, p1, p2):
        self.parent1 = p1
        self.parent2 = p2

    def add_metric(self, key, val):
        self.metrics[key] = val

    def get_metric(self, key, val):
        pass

    def __clear_metrics__(self):
        self.metrics = {}

def generate_random_chromosome(size):
    return random.randint(0, 2 ** (size - 1) +1)

