import math
import numpy as np
from numpy.linalg import inv, det

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
        self.speed_influence = 0
        self.direction = direction
        self.color = "green"

    def update(self, rectangles):
        self.speed_influence = 0
        self.color = "green"
        if self.check_pointer_hit_rectangle(rectangles):
            self.color = "red"
            self.speed_influence = self.speed

    def check_pointer_hit_rectangle(self, rectangles):
        pointer_const = [self.current_x, self.current_y]
        pointer_vector = [self.width, self.height]
        for rectangle in rectangles:
            # bottom segment
            constant = [rectangle.current_x, rectangle.current_y + rectangle.height]
            vector = [rectangle.width, 0]
            if self.__line_segments_intersect__(pointer_const, pointer_vector, constant, vector):
                return True
            # left segment
            constant = [rectangle.current_x, rectangle.current_y]
            vector = [0, rectangle.height]
            print(constant, vector)
            if self.__line_segments_intersect__(pointer_const, pointer_vector, constant, vector):
                return True
            # right segment
            constant = [rectangle.current_x + rectangle.width, rectangle.current_y]
            vector = [0, rectangle.height]
            if self.__line_segments_intersect__(pointer_const, pointer_vector, constant, vector):
                return True
        return False

    @staticmethod
    def __line_segments_intersect__(constant_1, vector_1, constant_2, vector_2):
        vector_2 = -1 * np.array(vector_2)
        vector_1 = np.array(vector_1)
        matrix_1 = np.vstack((vector_1, vector_2)).T
        const_vector = np.vstack(np.array(constant_2) - np.array(constant_1))
        if det(matrix_1) == 0:
            return False
        inverse = np.linalg.inv(matrix_1)
        val = np.matmul(inverse, const_vector)
        return (val >= 0).all() and (val <= 1).all()

    def create_gui_object(self, frame):
        self.gui_object = frame.create_line(*self.current_location(), fill=self.color, width="2")

    def update_gui_object(self, frame):
        frame.itemconfig(self.gui_object, fill=self.color)
