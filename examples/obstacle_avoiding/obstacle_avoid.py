import time

from examples.obstacle_avoiding.game_objects.player import Player
from examples.obstacle_avoiding.game_objects.obstacle import Obstacle
from examples.obstacle_avoiding.obstace_avoid_constants import *
from examples.obstacle_avoiding.obstacle_avoid_gui import update_gui_objects

from src.individual import Individual
from src.chromosome import generate_random_chromosome



'''
Genetic Algorithm Explanation:

A box tries to avoid obstacles that falls down on it
The box has three pointers that allow it to move accordingly
The pointers can have varying angles from (1, 180) and lengths from (5, 20) px
If the pointer is activated the box will move in a certain direction

angle: 180 (8 bits) val/255*180
length: 40-150 (7 bits) val/127*110 + 40
speed: 0-7 (3 bits)
direction: 0-1 (1 bit)

3 pointers: 3*(8 + 7 + 3 + 1) = 57
Player dies when an obstacle hits it
'''
# setup functions
def parse_genes(individual):
    current_gene = 1
    angle1 = individual.gene_value(current_gene, current_gene + ANGLE_GENE_SIZE - 1)
    angle2 = individual.gene_value(current_gene + ANGLE_GENE_SIZE - 1, current_gene + 2 * ANGLE_GENE_SIZE - 1)
    angle3 = individual.gene_value(current_gene + 2 * ANGLE_GENE_SIZE - 1, current_gene + 3 * ANGLE_GENE_SIZE - 1)
    current_gene += 3 * ANGLE_GENE_SIZE - 1
    length1 = individual.gene_value(current_gene, current_gene + LENGTH_GENE_SIZE - 1)
    length2 = individual.gene_value(current_gene + LENGTH_GENE_SIZE - 1, current_gene + 2 * LENGTH_GENE_SIZE - 1)
    length3 = individual.gene_value(current_gene + 2 * LENGTH_GENE_SIZE - 1, current_gene + 3 * LENGTH_GENE_SIZE - 1)
    current_gene += 3 * LENGTH_GENE_SIZE - 1
    speed1 = individual.gene_value(current_gene, current_gene + SPEED_GENE_SIZE - 1)
    speed2 = individual.gene_value(current_gene + SPEED_GENE_SIZE - 1, current_gene + 2 * SPEED_GENE_SIZE - 1)
    speed3 = individual.gene_value(current_gene + 2 * SPEED_GENE_SIZE - 1, current_gene + 3 * LENGTH_GENE_SIZE - 1)
    current_gene += 3 * SPEED_GENE_SIZE - 1
    direction1 = individual.gene_value(current_gene, current_gene + DIRECTION_GENE_SIZE - 1)
    direction2 = individual.gene_value(current_gene + DIRECTION_GENE_SIZE - 1,
                                       current_gene + 2 * DIRECTION_GENE_SIZE - 1)
    direction3 = individual.gene_value(current_gene + 2 * DIRECTION_GENE_SIZE - 1,
                                       current_gene + 3 * DIRECTION_GENE_SIZE - 1)
    return ((angle1, angle2, angle3), (length1, length2, length3), (speed1, speed2, speed3),
            (direction1, direction2, direction3))


def create_player(individual, frame=None):
    player = Player(*parse_genes(individual))
    if frame is not None:
        player.create_gui_object(frame)
    return player


def create_obstacle(frame=None):
    obstacle = Obstacle()
    if frame is not None:
        obstacle.create_gui_object(frame)
    return obstacle


def setup_players(individuals, frame=None):
    players = []
    for individual in individuals:
        player = create_player(individual, frame=frame)
        players.append(player)
    return players


def setup_obstacles(frame=None):
    obstacle = create_obstacle(frame=frame)
    return [obstacle]


# update functions
def update_all_players(players, obstacles, delta):
    for player in players:
        player.update(delta, obstacles)


def update_all_obstacles(obstacles, delta):
    for obstacle in obstacles:
        obstacle.update(delta)


def check_to_remove_obstacle(obstacles):
    if obstacles[0].is_past_frame():
        return True
    return False


def check_to_add_obstacle(total_delta):
    if total_delta >= OBSTACLE_ADDITION_PERIOD:
        return True
    return False


# processing functions
def process_generation(individuals):
    pass


def run_main_loop(window=None, frame=None):
    delta = 0
    obstacle_addition_delta = 0

    # initial setup of obstacles
    obstacles = setup_obstacles(frame=frame)

    # initial setup of players
    #individual = Individual(PLAYER_CHROMOSOME_LENGTH, chromosome=generate_random_chromosome(PLAYER_CHROMOSOME_LENGTH))
    #players = setup_players([individual], frame=frame)

    # main loop
    while True:
        start_time = time.time()

        # update obstacles
        update_all_obstacles(obstacles, delta)
        if check_to_add_obstacle(obstacle_addition_delta):
            obstacles.append(create_obstacle(frame=frame))
            obstacle_addition_delta -= OBSTACLE_ADDITION_PERIOD
        if check_to_remove_obstacle(obstacles):
            obstacle = obstacles.pop(0)
            if frame is not None:
                obstacle.delete_gui_object(frame)

        # update gui if window created
        if window is not None and frame is not None:
            update_gui_objects(frame, obstacles)
            window.update_idletasks()
            window.update()

        # update game thread
        sleep_time = TIME_GAP_IN_SECONDS - (time.time() - start_time)
        if sleep_time < 0:
            sleep_time = 0
        time.sleep(sleep_time)
        print(len(obstacles))
        delta = time.time() - start_time
        obstacle_addition_delta += delta


if __name__ == '__main__':
    run_main_loop()
