import random

from examples.obstacle_avoiding.obstace_avoid_constants import *
from examples.obstacle_avoiding.game_object import GameObject


class Obstacle(GameObject):
    def __init__(self):
        x1 = int(random.random()*FRAME_WIDTH - OBSTACLE_WIDTH/2)
        GameObject.__init__(self, x1, 0, x1 + OBSTACLE_WIDTH, OBSTACLE_HEIGHT)

    def update(self, delta):
        self.previous_y = self.current_y
        self.current_y += delta*OBSTACLE_SPEED

    def is_past_frame(self):
        return self.current_y >= FRAME_HEIGHT
