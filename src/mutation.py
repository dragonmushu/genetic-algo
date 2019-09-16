from abc import ABC, abstractmethod
import random

from src.individual import Individual
from src.utils import flip_bit


class Mutation(ABC):
    @abstractmethod
    def mutate(self, individual: Individual) -> Individual:
        pass


class FlipMutation(Mutation):
    def __init__(self, chromosome_size, mutation_rate=0.001):
        self.mutation_rate = mutation_rate
        self.chromosome_size = chromosome_size

    def mutate(self, chromosome: int) -> int:
        for position in range(1, self.chromosome_size + 1):
            if random.random() < self.mutation_rate:
                chromosome = flip_bit(chromosome, position)
        return chromosome

