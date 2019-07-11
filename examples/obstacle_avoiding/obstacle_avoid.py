import time

from examples.obstacle_avoiding.game_objects.player import Player
from examples.obstacle_avoiding.game_objects.obstacle import Obstacle
from examples.obstacle_avoiding.obstace_avoid_constants import *
from examples.obstacle_avoiding.obstacle_avoid_gui import update_gui_objects

'''
Genetic Algorithm Explanation:

A box tries to avoid obstacles that falls down on it
The box has three pointers that allow it to move accordingly
The pointers can have varying angles from (1, 180) and lengths from (5, 20) px
If the pointer is activated the box will move in a certain direction

angle: 180 (8 bits) val/255*180
length: 40-150 (7 bits) val/127*110 + 40
speed: 0-15 (4 bits)
direction: 0-1 (1 bit)

3 pointers: 3*(8 + 7 + 3 + 1) = 57
Player dies when an obstacle hits it
'''


# setup functions
def parse_genes(individual):
    current_gene = 1
    angles = [individual.gene_value(current_gene + i * ANGLE_GENE_SIZE, current_gene +
                                    (i + 1) * ANGLE_GENE_SIZE - 1) for i in range(0, PLAYER_POINTERS)]
    current_gene += PLAYER_POINTERS * ANGLE_GENE_SIZE
    lengths = [individual.gene_value(current_gene + i * LENGTH_GENE_SIZE, current_gene +
                                     (i + 1) * LENGTH_GENE_SIZE - 1) for i in range(0, PLAYER_POINTERS)]
    current_gene += PLAYER_POINTERS * LENGTH_GENE_SIZE
    speeds = [individual.gene_value(current_gene + i * SPEED_GENE_SIZE, current_gene +
                                    (i + 1) * SPEED_GENE_SIZE - 1) for i in range(0, PLAYER_POINTERS)]
    current_gene += PLAYER_POINTERS * SPEED_GENE_SIZE
    directions = [individual.gene_value(current_gene + i * DIRECTION_GENE_SIZE, current_gene +
                                        (i + 1) * DIRECTION_GENE_SIZE - 1) for i in range(0, PLAYER_POINTERS)]
    return angles, lengths, speeds, directions


def create_player(individual, frame=None):
    player = Player(*parse_genes(individual), individual)
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


def check_and_update_players(players, obstacle, total_time, frame=None):
    new_players = []
    for player in players:
        if player.check_hit_wall() or player.check_hit_obstacle(obstacle):
            if frame is not None:
                player.delete_gui_object(frame)
            player.individual.add_metric("time", total_time)
        else:
            new_players.append(player)
    return new_players


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


def run_main_loop(players, window=None, frame=None):
    total_time = 0
    delta = 0
    obstacle_addition_delta = 0

    # initial setup of obstacles
    obstacles = setup_obstacles(frame=frame)
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

        # update player
        update_all_players(players, obstacles, delta)
        players = check_and_update_players(players, obstacles[0], total_time, frame=frame)

        # break loop when players are all
        if not players:
            if window is not None:
                window.destroy()
            return

        # update gui if window created
        if window is not None and frame is not None:
            update_gui_objects(frame, obstacles)
            update_gui_objects(frame, players)
            window.update_idletasks()
            window.update()

        # update game thread
        sleep_time = TIME_GAP_IN_SECONDS - (time.time() - start_time)
        if sleep_time < 0:
            sleep_time = 0
        time.sleep(sleep_time)
        delta = time.time() - start_time
        obstacle_addition_delta += delta
        total_time += delta


#
