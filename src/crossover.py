import random
import src.utils as utils


def cross_with_mask(val_1, val_2, mask):
    return utils.apply_mask(val_1, mask) | utils.apply_mask(val_2, ~mask)


def create_offspring_from_mask(chromosome_1: int, chromosome_2: int, mask: int) -> tuple(int, int):
    offspring_1 = cross_with_mask(chromosome_2, chromosome_1, mask)
    offspring_2 = cross_with_mask(chromosome_1, chromosome_2, mask)
    return offspring_1, offspring_2


def point_cross_over(chromosome_1: int, chromosome_2: int, size: int, point: int) -> tuple(int, int):
    max_val = utils.max_binary_value(size)
    mask = utils.shift_bytes(max_val, point)
    return create_offspring_from_mask(chromosome_1, chromosome_2, mask)


def single_point_cross_over(chromosome_1: int, chromosome_2: int, size: int) -> tuple(int, int):
    random_point = random.randint(1, size)
    return point_cross_over(chromosome_1, chromosome_2, size, random_point)


def center_cross_over(chromosome_1: int, chromosome_2: int, size: int) -> tuple(int, int):
    center = int(size/2)
    return point_cross_over(chromosome_1, chromosome_2, size, center)


def junction_cross_over(chromosome_1: int, chromosome_2: int, size: int, point_1: int, point_2: int) -> tuple(int, int):
    max_val = utils.max_binary_value(size)
    mask_1 = utils.shift_bytes(max_val, point_1)
    mask_2 = utils.shift_bytes(max_val, point_2)
    mask = mask_1 | ~mask_2
    return create_offspring_from_mask(chromosome_1, chromosome_2, mask)


def random_junction_cross_over(chromosome_1: int, chromosome_2: int, size: int) -> tuple(int, int):
    point_1 = random.randint(0, size + 1)
    point_2 = random.randint(0, size + 1)
    return junction_cross_over(chromosome_1, chromosome_2, size, point_1, point_2)


def uniform_cross_over(chromosome_1: int, chromosome_2: int, size: int, probability: float) -> tuple(int, int):
    mask_bits = ""
    for i in range(0, size):
        if random.random() < probability:
            mask += "1"
        else:
            mask += "0"
    mask = int(mask_bits, 2)
    return create_offspring_from_mask(chromosome_1, chromosome_2, mask)


def random_probability_uniform_cross_over(chromosome_1: int, chromosome_2: int, size: int) -> tuple(int, int):
    probability = random.random()
    return uniform_cross_over(chromosome_1, chromosome_2, size, probability)