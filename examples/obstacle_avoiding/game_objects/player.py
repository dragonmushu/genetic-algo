from examples.obstacle_avoiding.game_objects.game_object import GameObject
from examples.obstacle_avoiding.game_objects.pointer import Pointer
from examples.obstacle_avoiding.obstace_avoid_constants import *


class Player(GameObject):
    def __init__(self, pointer_angles, pointer_lengths, speeds, directions, individual):
        GameObject.__init__(self, int(FRAME_WIDTH / 2 - PLAYER_WIDTH / 2), FRAME_HEIGHT - PLAYER_HEIGHT,
                            int(FRAME_WIDTH / 2 - PLAYER_WIDTH / 2) + PLAYER_WIDTH, FRAME_HEIGHT)
        self.pointers = [Pointer(pointer_angles[i], pointer_lengths[i], speeds[i], directions[i]) for i in range(0, 3)]
        self.individual = individual
        self.current_speed = 0

    def update(self, delta, obstacles):
        if len(obstacles) >= 3:
            rectangles = [obstacles[i] for i in range(0, 3)]
            for pointer in self.pointers:
                pointer.update_influence(rectangles)
                self.current_speed += pointer.speed_influence
            for pointer in self.pointers:
                pointer.update(delta, self.current_speed)
            self.previous_x = self.current_x
            self.current_x += delta*self.current_speed

    def create_gui_object(self, frame):
        for pointer in self.pointers:
            pointer.create_gui_object(frame)
        self.gui_object = frame.create_rectangle(*self.current_location(), fill="black", outline="red")

    def update_gui_object(self, frame):
        GameObject.update_gui_object(self, frame)
        for pointer in self.pointers:
            pointer.update_gui_object(frame)

    def check_hit_wall(self):
        return self.current_x <= 0 or self.current_x + self.width >= FRAME_WIDTH

    def check_hit_obstacle(self, obstacle):
        not_overlap = self.current_x > obstacle.current_x + obstacle.width \
                      or obstacle.current_x > self.current_x + self.width \
                      or self.current_y > obstacle.current_y + obstacle.height \
                      or obstacle.current_y > self.current_y + self.height
        return not not_overlap

    def delete_gui_object(self, frame):
        GameObject.delete_gui_object(self, frame)
        for pointer in self.pointers:
            pointer.delete_gui_object(frame)
