from examples.obstacle_avoiding.game_objects.game_object import GameObject
from examples.obstacle_avoiding.game_objects.pointer import Pointer
from examples.obstacle_avoiding.obstace_avoid_constants import *


class Player(GameObject):
    def __init__(self, pointer_angles, pointer_lengths, speeds, directions):
        GameObject.__init__(self, int(FRAME_WIDTH / 2 - PLAYER_WIDTH / 2), FRAME_HEIGHT - PLAYER_HEIGHT,
                            int(FRAME_WIDTH / 2 - PLAYER_WIDTH / 2) + PLAYER_WIDTH, FRAME_HEIGHT)
        self.pointers = [Pointer(pointer_angles[i], pointer_lengths[i], speeds[i], directions[i]) for i in range(0, 3)]

    def update(self, delta, obstacles):
        pass

    def create_gui_object(self, frame):
        for pointer in self.pointers:
            pointer.create_gui_object(frame)
        self.gui_object = frame.create_rectangle(*self.current_location())

    def move_gui_object(self, frame):
        frame.move(*self.delta_position())
        for pointer in self.pointers:
            pointer.move_gui_object(frame)
