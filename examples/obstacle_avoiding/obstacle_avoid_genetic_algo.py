from src.genetic_algo import GenGo

from examples.obstacle_avoiding.obstace_avoid_constants import PLAYER_CHROMOSOME_LENGTH
from examples.obstacle_avoiding.obstacle_avoid import setup_players, run_main_loop
from examples.obstacle_avoiding.obstacle_avoid_gui import setup_gui


# processing functions
def process_generation(individuals):
    # initial setup of players
    players = setup_players(individuals)
    run_main_loop(players)


def process_generation_gui(individuals):
    # initial setup of players
    players = setup_players(individuals)
    run_main_loop(players, *setup_gui())


# fitness function
def fitness_function(individual):
    return individual.get_metric("time")


gengo = GenGo(chromosome_size=PLAYER_CHROMOSOME_LENGTH, population_size=5)
gengo.process_batch(process_generation_gui).fitness(fitness_function).run()

