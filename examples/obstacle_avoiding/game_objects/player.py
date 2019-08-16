from examples.obstacle_avoiding.game_objects.game_object import GameObject
from examples.obstacle_avoiding.game_objects.pointer import Pointer
from examples.obstacle_avoiding.obstace_avoid_constants import *


class Player(GameObject):
    def __init__(self, pointer_angles, pointer_lengths, speeds, directions, individual):
        GameObject.__init__(self, int(FRAME_WIDTH / 2 - PLAYER_WIDTH / 2), FRAME_HEIGHT - PLAYER_HEIGHT,
                            int(FRAME_WIDTH / 2 - PLAYER_WIDTH / 2) + PLAYER_WIDTH, FRAME_HEIGHT)
        self.speeds = list(speeds)
        self.directions = list(directions)
        for i in range(0, len(directions)):
            self.directions[i] = self.directions[i] * -2 + 1
        self.pointers = [Pointer(pointer_angles[i], pointer_lengths[i]) for i in range(0, 3)]
        self.individual = individual
        self.current_speed = 0

    def update(self, delta, obstacles):
        if len(obstacles) >= 3:
            rectangles = [obstacles[i] for i in range(0, 3)]
            pointers_hit = [False for _ in range(0, len(self.pointers))]
            index = 0
            for pointer in self.pointers:
                if pointer.update_pointer_hit(rectangles):
                    pointers_hit[index] = True
                index += 1
            self.current_speed += self.update_speed(pointers_hit)
            for pointer in self.pointers:
                pointer.update(delta, self.current_speed)
            self.previous_x = self.current_x
            self.current_x += delta*self.current_speed

    def update_speed(self, pointers_hit):
        if pointers_hit[0] and pointers_hit[1] and pointers_hit[2]:
            return self.directions[0] * self.speeds[0] * SPEED_FACTOR
        elif pointers_hit[0] and pointers_hit[1]:
            return self.directions[1] * self.speeds[1] * SPEED_FACTOR
        elif pointers_hit[0] and pointers_hit[2]:
            return self.directions[2] * self.speeds[2] * SPEED_FACTOR
        elif pointers_hit[1] and pointers_hit[2]:
            return self.directions[3] * self.speeds[3] * SPEED_FACTOR
        elif pointers_hit[0]:
            return self.directions[4] * self.speeds[4] * SPEED_FACTOR
        elif pointers_hit[1]:
            return self.directions[5] * self.speeds[5] * SPEED_FACTOR
        elif pointers_hit[2]:
            return self.directions[6] * self.speeds[6] * SPEED_FACTOR
        return 0

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
