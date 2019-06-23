def max_binary_value(size):
    if size == 0:
        return 0
    return 2 ** size - 1


def shift_bytes(val, point):
    return val >> point


def apply_mask(val, mask):
    return val & mask
