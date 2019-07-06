from src.genetic_algo import GenGo

from examples.obstacle_avoiding.obstace_avoid_constants import PLAYER_CHROMOSOME_LENGTH
from examples.obstacle_avoiding.obstacle_avoid import setup_players, run_main_loop
from examples.obstacle_avoiding.obstacle_avoid_gui import setup_gui

generation = 0  # generation number

# processing functions
def process_generation(individuals):
    # initial setup of players
    players = setup_players(individuals)
    run_main_loop(players)


def process_generation_gui(individuals):
    # initial setup of players
    window, frame = setup_gui()
    players = setup_players(individuals, frame=frame)
    run_main_loop(players, window=window, frame=frame)


# fitness function
def fitness_function(individual):
    return individual.get_metric("time")


gengo = GenGo(chromosome_size=PLAYER_CHROMOSOME_LENGTH, population_size=100)
gengo.process_batch(process_generation).fitness(fitness_function).run()
