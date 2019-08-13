from abc import ABC, abstractmethod
from typing import Tuple

import random
import src.utils as utils
from src.individual import Individual


def cross_with_mask(val_1, val_2, mask):
    return utils.apply_mask(val_1, mask) | utils.apply_mask(val_2, ~mask)


def create_offspring_from_mask(chromosome_1: int, chromosome_2: int, mask: int) -> Tuple[int, int]:
    offspring_1 = cross_with_mask(chromosome_2, chromosome_1, mask)
    offspring_2 = cross_with_mask(chromosome_1, chromosome_2, mask)
    return offspring_1, offspring_2


def point_cross_over(chromosome_1: int, chromosome_2: int, size: int, point: int) -> Tuple[int, int]:
    max_val = utils.max_binary_value(size)
    mask = utils.shift_bytes(max_val, point)
    return create_offspring_from_mask(chromosome_1, chromosome_2, mask)


def junction_cross_over(chromosome_1: int, chromosome_2: int, size: int, point_1: int, point_2: int) -> Tuple[int, int]:
    max_val = utils.max_binary_value(size)
    mask_1 = utils.shift_bytes(max_val, point_1)
    mask_2 = utils.shift_bytes(max_val, point_2)
    mask = mask_1 | ~mask_2
    return create_offspring_from_mask(chromosome_1, chromosome_2, mask)


def uniform_cross_over(chromosome_1: int, chromosome_2: int, size: int, probability: float) -> Tuple[int, int]:
    mask_bits = ""
    for i in range(0, size):
        if random.random() < probability:
            mask += "1"
        else:
            mask += "0"
    mask = int(mask_bits, 2)
    return create_offspring_from_mask(chromosome_1, chromosome_2, mask)


class CrossOver(ABC):
    @abstractmethod
    def crossover(self, individual_1: Individual, individual_2: Individual) -> Tuple[int, ...]:
        pass


class SinglePointCross(CrossOver):
    @staticmethod
    def crossover(individual_1: Individual, individual_2: Individual) -> Tuple[int, int]:
        size = individual_1.chromosome_size
        random_point = random.randint(1, size)
        return point_cross_over(individual_1.chromosome, individual_2.chromosome, size, random_point)


class CenterCross(CrossOver):
    @staticmethod
    def crossover(individual_1: Individual, individual_2: Individual) -> Tuple[int, int]:
        size = individual_1.chromosome_size
        center = int(size / 2)
        return point_cross_over(individual_1.chromosome, individual_2.chromosome, size, center)


class RandomUniformCross(CrossOver):
    @staticmethod
    def crossover(individual_1: Individual, individual_2: Individual) -> Tuple[int, int]:
        probability = random.random()
        size = individual_1.chromosome_size
        return uniform_cross_over(individual_1.chromosome, individual_2.chromosome, size, probability)


class RandomJunctionCross(CrossOver):
    @staticmethod
    def crossover(individual_1: Individual, individual_2: Individual) -> Tuple[int, int]:
        size = individual_1.chromosome_size
        point_1 = random.randint(0, size + 1)
        point_2 = random.randint(0, size + 1)
        return junction_cross_over(individual_1.chromosome, individual_2.chromosome, size, point_1, point_2)

