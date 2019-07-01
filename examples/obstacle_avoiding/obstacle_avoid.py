import time

from examples.obstacle_avoiding.player import Player
from examples.obstacle_avoiding.obstacle import Obstacle
from examples.obstacle_avoiding.obstace_avoid_constants import *


def update_all_players(players, obstacles, delta):
    for player in players:
        player.update(delta, obstacles)


def update_all_obstacles(obstacles, delta):
    for obstacle in obstacles:
        obstacle.update(delta)


def check_and_remove_obstacle(obstacles):
    if obstacles[-1].is_past_frame():
        obstacles.pop()


def add_new_obstacle_to_list(obstacles):
    obstacles.append(Obstacle())


'''
Processing Functions
'''
def setup_players(individuals):
    players = [Player((0)) for individual in individuals]


def setup_obstacles(obstacles):
    add_new_obstacle_to_list()


def process_generation(individuals):
    pass


def run_main_loop():
    delta = 0
    obstacle_addition_delta = 0
    obstacles = []
    add_new_obstacle_to_list(obstacles)
    while True:
        start_time = time.time()
        delta = time.time() - start_time
        time.sleep(TIME_GAP_IN_SECONDS - delta)
        delta = time.time() - start_time


if __name__ == '__main__':
    run_main_loop()
