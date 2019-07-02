import math

from examples.obstacle_avoiding.game_objects.game_object import GameObject
from examples.obstacle_avoiding.obstace_avoid_constants import *


class Pointer(GameObject):
    def __init__(self, angle, length, speed, direction):
        self.angle = math.radians(angle/255*180)
        self.length = length/127*110 + 40
        x1 = FRAME_WIDTH/2
        y1 = FRAME_HEIGHT - PLAYER_HEIGHT/2
        GameObject.__init__(self, x1, y1, x1 - self.length * math.cos(self.angle),
                            y1 - self.length * math.sin(self.angle))
        self.speed = speed
        self.direction = direction

    def check_pointer_hit_rectangle(self, rectangles):
        pass

    def create_gui_object(self, frame):
        self.gui_object = frame.create_line(*self.current_location())
