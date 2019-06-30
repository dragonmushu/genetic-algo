import random
import time

from examples.obstacle_avoiding.obstace_avoid_constants import *


all_rectangles = []


def update_player_position(total_delta):
    pass


def add_new_rectangle_to_list(total_delta):
    all_rectangles.append(random_rectangle_at_top())


def update_all_rectangle_positions(total_delta):
    pixels_moved = int(total_delta * RECTANGLE_HEIGHT_SPEED)
    for index, rectangle in enumerate(all_rectangles):
        all_rectangles[index] = (rectangle[0], rectangle[1] + pixels_moved, rectangle[3], rectangle[4] +
                                 pixels_moved)


def check_and_remove_rectangle():
    if all_rectangles[-1][1] >= FRAME_HEIGHT:
        all_rectangles.pop()


def random_rectangle_at_top():
    x_location = int(random.random()*FRAME_WIDTH - RECTANGLE_WIDTH/2)
    y_location = 0
    return x_location, y_location, x_location + RECTANGLE_WIDTH, y_location + RECTANGLE_HEIGHT


'''
Processing Functions
'''
def process_generation(individuals):
    pass


def run_main_loop():
    total_delta = 0
    while True:
        start_time = time.time()
        update_all_rectangle_positions(total_delta)

        check_and_remove_rectangle()
        delta = time.time() - start_time
        time.sleep(TIME_GAP_IN_SECONDS - delta)
        total_delta += time.time() - start_time


if __name__ == '__main__':
    run_main_loop()
