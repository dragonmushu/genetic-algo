from typing import List, Tuple
import random

from src.individual import Individual

# TODO: implement binary search for finding individual in roulette probability list
def roulette_binary_search(values: List[int], target: int) -> int:
    pass


def roulette_probability(values: List[int]) -> List[int]:
    sum = sum(values)
    probability_distribution = [values[0]/sum]
    for i in range(1, len(values)):
        probability_distribution.append((values[i - 1] + values[i])/sum)
    return probability_distribution


def roulette_wheel_select_parent(individuals: List[Individual]) -> int:
    fitness_values = [individual.fitness for individual in individuals]
    probability_distribution = roulette_probability(fitness_values)
    probability = random.random()
    index = 0
    while probability > probability_distribution[index]:
        index += 1
    return individuals[index]


def roulette_wheel_selection(individuals: List[Individual]) -> Tuple[Individual, Individual]:
    individuals_temp = individuals.copy()
    parent_1 = roulette_wheel_select_parent(individuals_temp)
    individuals_temp.remove(parent_1)
    parent_2 = roulette_wheel_select_parent(individuals_temp)
    return parent_1, parent_2



