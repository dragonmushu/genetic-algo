import time

from examples.obstacle_avoiding.player import Player
from examples.obstacle_avoiding.obstacle import Obstacle
from examples.obstacle_avoiding.obstace_avoid_constants import *

'''
Genetic Algorithm Explanation:

A box tries to avoid obstacles that falls down on it
The box has three pointers that allow it to move accordingly
The pointers can have varying angles from (1, 180) and lengths from (5, 20) px
If the pointer is activated the box will move in a certain direction

angle: 180 (8 bits) int(val/255*180)
length: 5-20 (4 bits) int(val/15*11) + 5
speed: 0-7 (3 bits)
direction: 0-1 (1 bit)

3 pointers: 3*(8 + 4 + 3 + 1) = 48
Player dies when an obstacle hits it
'''


# setup functions
def setup_players(individuals):
    for individual in individuals:
        angle1 = individual.gene_value()
        players = [Player((0)) for individual in individuals]


def setup_obstacles(obstacles):
    add_new_obstacle_to_list()


# update functions
def update_all_players(players, obstacles, delta):
    for player in players:
        player.update(delta, obstacles)


def update_all_obstacles(obstacles, delta):
    for obstacle in obstacles:
        obstacle.update(delta)


def check_to_remove_obstacle(obstacles):
    if obstacles[-1].is_past_frame():
        return True
    return False


def check_to_add_obstacle(obstacles, total_delta):
    if total_delta >= OBSTACLE_ADDITION_PERIOD:
        return True
    return False


def add_new_obstacle_to_list(obstacles):
    obstacle = Obstacle()
    obstacles.append(obstacle)
    return obstacle


# processing functions
def process_generation(individuals):
    pass


def run_main_loop():
    delta = 0
    obstacle_addition_delta = 0
    obstacles = []

    # initial setup of obstacles
    setup_obstacles(obstacles)

    # initial setup of players

    # main loop
    while True:
        start_time = time.time()

        # update obstacles
        update_all_obstacles(obstacles, delta)
        if check_to_add_obstacle(obstacles, obstacle_addition_delta):
            add_new_obstacle_to_list(obstacles)
            obstacle_addition_delta -= OBSTACLE_ADDITION_PERIOD
        if check_to_remove_obstacle(obstacles):
            obstacles.pop()

        # update game thread
        delta = time.time() - start_time
        time.sleep(TIME_GAP_IN_SECONDS - delta)
        delta = time.time() - start_time
        obstacle_addition_delta += delta


if __name__ == '__main__':
    run_main_loop()
