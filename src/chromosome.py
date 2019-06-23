import random


def generate_random_chromosome(size):
    if size == 0:
        return 0
    return random.randint(0, 2 ** size)


def generate_chromosome_from_bits(bits):
    return int(bits, 2)
