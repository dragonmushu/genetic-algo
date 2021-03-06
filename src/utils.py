import random


def max_binary_value(size):
    if size == 0:
        return 0
    return 2 ** size - 1


def shift_bytes(val, point):
    return val >> point


def apply_mask(val, mask):
    return val & mask


def bit_set(val, position):
    temp = 1 << (position - 1)
    return temp & val != 0


def set_bit(val, position):
    temp = 1 << (position - 1)
    return temp | val


def unset_bit(val, position):
    temp = 1 << (position - 1)
    return (~temp) & val


def flip_bit(val, position):
    if bit_set(val, position):
        return unset_bit(val, position)
    return set_bit(val, position)


def random_two_elements(elements):
    if len(elements) < 2:
        raise Exception('List size less than two')
    return random.sample(elements, 2)