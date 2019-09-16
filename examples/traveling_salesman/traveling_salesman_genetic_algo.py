from examples.traveling_salesman.traveling_salesman import random_distances
from examples.traveling_salesman.traveling_salesman_constants import *

distances = {}

# setup callback
def setup_problem(gengo):
    global distances
    distances = random_distances(NUMBER_CITIES, max_distance=100)


# processing function
def process_generation(individuals):
    process_paths
