from abc import ABC, abstractmethod
from typing import List, Tuple
import random

from src.individual import Individual


class Selection(ABC):
    @abstractmethod
    def select_parents(self, individuals: List[Individual]) -> Tuple[Individual, Individual]:
        pass


class RandomSelection(Selection):
    @staticmethod
    def select_parents(self, individuals: List[Individual]) -> Tuple[Individual, Individual]:
        return random.sample(individuals, 2)


class RouletteWheel(Selection):
    # TODO: implement binary search for finding individual in roulette probability list
    def binary_search(self, values: List[int], target: int):
        pass

    # TODO: Extract this function to utils (common probability distribution)
    @staticmethod
    def create_probability_distribution(values: List[int]) -> List[int]:
        total = sum(values)
        probability_distribution = [values[0] / total]
        for i in range(1, len(values)):
            probability_distribution.append((values[i - 1] + values[i]) / total)
        return probability_distribution

    @staticmethod
    def select_single_parent(self, individuals: List[Individual]) -> Individual:
        fitness_values = [individual.fitness for individual in individuals]
        probability_distribution = self.create_probability_distribution(fitness_values)
        probability = random.random()
        index = 0
        # TODO: Change to binary search
        while probability > probability_distribution[index]:
            index += 1
        return individuals[index]

    @staticmethod
    def select_parents(self, individuals: List[Individual]) -> Tuple[Individual, Individual]:
        individuals_temp = individuals.copy()
        parent_1 = self.select_single_parent(individuals_temp)
        individuals_temp.remove(parent_1)
        parent_2 = self.select_single_parent(individuals_temp)
        return parent_1, parent_2


'''
Stochastic Remainder Selection

Selection based on having individuals have fixed number of progeny they can create.
The integer value of normalized fitness (fitness / avg) represents definite progeny.
The remainder goes through Roulette wheel selection until population limit is reached.

The number of children produced per parent has to be fixed for this algorithm
'''
class StochasticRemainder(Selection):
    def __init__(self, total_population: int, fraction_fixed_progeny: float, children_per_parent=2):
        self.definite_parents = {}
        self.total_population = total_population
        self.fraction_fixed_progeny = fraction_fixed_progeny # scaling operation used for number of fixed progeny (estimation)
        self.children_per_parent = children_per_parent
        self.individuals = []  # need to store copy of individuals passed in

    # TODO: Extract this function to utils
    @staticmethod
    def normalized_fitness(values: List[int]) -> List[int]:
        avg = sum(values)/len(values)
        normalized_val = [val/avg for val in values]
        return normalized_val

    def initialize_selection(self, individuals: List[Individual]) -> Tuple[Individual, Individual]:
        self.individuals = individuals.copy()
        normalized_fitness_val = self.normalized_fitness([individual.fitness for individual in self.individuals])
        total_normalized_value = sum(normalized_fitness_val)
        definite_children = self.total_population * self.fraction_fixed_progeny
        fitness_multiplier = definite_children / total_normalized_value
        for i in range(0, len(individuals)):
            fitness = int(normalized_fitness_val[i] * fitness_multiplier)
            if fitness > 0:
                self.definite_parents[self.individuals[i]] = fitness
            self.individuals[i].fitness -= fitness

    def select_parents(self, individuals: List[Individual]) -> Tuple[Individual, Individual]:
        if self.definite_parents:
            parent_1, parent_2 = RandomSelection.select_parents(list(self.definite_parents.keys()))
            self.definite_parents[parent_1] -= self.children_per_parent
            self.definite_parents[parent_2] -= self.children_per_parent
            if self.definite_parents[parent_1] <= 0:
                del self.definite_parents[parent_1]
            if self.definite_parents[parent_2] <= 0:
                del self.definite_parents[parent_2]
        else:
            return RouletteWheel.select_parents(self.individuals)











