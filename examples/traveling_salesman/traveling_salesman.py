import random

from examples.traveling_salesman.traveling_salesman_constants import *


def random_distances(number_cities, max_distance=10):
    distances = {}
    for i in range(1, number_cities + 1):
        for t in range(i + 1, number_cities + 1):
            distances[(i, t)] = random.random() * max_distance
    return distances


def genes_to_value(individual, gene_size, number_cities):
    values = [individual.gene_value(1 + i * gene_size, 1 +
                                    (i + 1) * gene_size - 1) for i in range(0, number_cities)]
    return values


def path_to_take(individual, gene_size, number_cities):
    values = genes_to_value(individual, gene_size, number_cities)
    ordered_values = values.copy()
    ordered_values.sort()
    cities = {}
    current_city = 1
    for val in ordered_values:
        if val in cities:
            cities[val].append(current_city)
        else:
            cities[val] = [current_city]
        current_city += 1
    path = []
    for val in values:
        path.append(cities[val].pop(0))
    return path


def calculate_distance(path, distances):
    total = 0
    for i in range(1, len(path)):
        city_1 = min(path[i - 1], path[i])
        city_2 = max(path[i - 1], path[i])
        total += distances(city_1, city_2)
    return total


def process_paths(individuals, distances):
    for individual in individuals:
        path = path_to_take(individual, NUMBER_CITIES, GENE_SIZE)
        individual.add_metric("distance", calculate_distance(path, distances))
