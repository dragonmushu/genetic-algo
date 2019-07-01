import random

from examples.obstacle_avoiding.obstace_avoid_constants import *


class Obstacle:
    def __init__(self):
        self.current_x = int(random.random()*FRAME_WIDTH - OBSTACLE_WIDTH/2)
        self.current_y = 0
        self.previous_x = self.current_x
        self.previous_y = self.current_y

    def update(self, delta):
        self.current_y += delta*OBSTACLE_SPEED

    def previous_location(self):
        return self.previous_x, self.previous_y, self.previous_x + OBSTACLE_WIDTH, self.previous_y + OBSTACLE_HEIGHT

    def current_location(self):
        return self.current_x, self.current_y, self.current_x + OBSTACLE_WIDTH, self.current_y + OBSTACLE_HEIGHT

    def is_past_frame(self):
        return self.current_y >= FRAME_HEIGHT
