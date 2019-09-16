from src.genetic_algo import GenGo

from examples.obstacle_avoiding.obstace_avoid_constants import PLAYER_CHROMOSOME_LENGTH
from examples.obstacle_avoiding.obstacle_avoid import setup_players, run_main_loop
from examples.obstacle_avoiding.obstacle_avoid_gui import setup_gui

generation = 0  # generation number
population_size = 10


# processing functions
# loop the processing three times to get an average
def process_generation(individuals):
    for _ in range(0, 3):
        # initial setup of players
        players = setup_players(individuals)
        run_main_loop(players)


def process_generation_gui(individuals):
    for _ in range(0, 3):
        # initial setup of players
        window, frame = setup_gui()
        players = setup_players(individuals, frame=frame)
        run_main_loop(players, window=window, frame=frame)


gengo = GenGo(chromosome_size=PLAYER_CHROMOSOME_LENGTH, population_size=population_size)
gengo.process(process_generation_gui, batch_size=10).fitness(lambda individual: individual.get_metric("time")).run()
