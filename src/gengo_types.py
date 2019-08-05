from enum import Enum


class ProcessTypes(Enum):
    BATCH = 0
    INDIVIDUAL = 1


class UserCallbackTypes(Enum):
    ITERATION_START = 0,
    AFTER_PROCESSING = 1,
    AFTER_FITNESS = 2,
    AFTER_SELECT_PARENTS = 3,
    AFTER_CROSSOVER = 4,
    AFTER_MUTATION = 5,
    ITERATION_END = 6
