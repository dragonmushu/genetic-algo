from examples.obstacle_avoiding.obstace_avoid_constants import *


class Player:
    def __init__(self, pointer_angles, pointer_lengths, speeds, directions):
        self.current_x = int(FRAME_WIDTH / 2 - PLAYER_WIDTH / 2)
        self.current_y = FRAME_HEIGHT - PLAYER_HEIGHT
        self.pointer_angles = pointer_angles
        self.pointer_lengths = pointer_lengths
        self.speeds = speeds
        self.directions = directions

    # update position of the player based on delta time
    def update(self, delta, obstacles):
        pass

    # check if the pointer hits a rectangle
    def __check_pointer_hit_rectangle__(self, pointer, obstacles):
        pass
