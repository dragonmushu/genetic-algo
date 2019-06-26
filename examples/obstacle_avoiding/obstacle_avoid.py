import random


FRAME_WIDTH = 400
FRAME_HEIGHT = 600

RECTANGLE_WIDTH = 80
RECTANGLE_HEIGHT = 10
RECTANGLE_HEIGHT_UPDATE = 5

PLAYER_WIDTH = 10
PLAYER_HEIGHT = 10

PLAYER_CHROMOSOME_LENGTH = 45
'''
Genetic Algorithm Explanation:

A box tries to avoid obstacles that falls down on it
The box has three pointers that allow it to move accordingly
The pointers can have varying angles from (1, 180) and lengths from (5, 20) px
If the pointer is activated the box will move in a certain direction

angle: 180 (8 bits) int(val/255*180)
length: 5-20 (4 bits) int(val/15*11) + 5
speed: 0-7 (3 bits)

3 pointers: 3*(8 + 4 + 3) = 45

Player dies when an obstacle hits it
'''


all_rectangles = []


def initial_player_location():
    x_location = int(FRAME_WIDTH/2 - PLAYER_WIDTH/2)
    y_location = FRAME_HEIGHT - PLAYER_HEIGHT
    return x_location, y_location, x_location + PLAYER_WIDTH, y_location + PLAYER_HEIGHT


def add_rectangle_to_list():
    all_rectangles.append(random_rectangle())


def update_all_rectangle_positions():
    for index, rectangle in enumerate(all_rectangles):
        all_rectangles[index] = (rectangle[0], rectangle[1] + RECTANGLE_HEIGHT_UPDATE, rectangle[3], rectangle[4] +
                                 RECTANGLE_HEIGHT_UPDATE)


def remove_rectangle():
    if all_rectangles[-1][1] >= FRAME_HEIGHT:
        all_rectangles.pop()


def random_rectangle():
    x_location = int(random.random()*FRAME_WIDTH - RECTANGLE_WIDTH/2)
    y_location = 0
    return x_location, y_location, x_location + RECTANGLE_WIDTH, y_location + RECTANGLE_HEIGHT



