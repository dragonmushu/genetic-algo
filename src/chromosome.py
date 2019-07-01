import random
import src.utils as utils


def generate_random_chromosome(size):
    if size == 0:
        return 0
    return random.randint(0, 2 ** size - 1)


def generate_chromosome_from_bits(bits):
    return int(bits, 2)


def chromosome_subset_value(chromosome, start, length):
    if start <= 0:
        raise ValueError('Start position has to be greater than or equal to 1')
    shifted_chromosome = utils.shift_bytes(chromosome, start - 1)
    mask = utils.max_binary_value(length)
    return utils.apply_mask(shifted_chromosome, mask)

