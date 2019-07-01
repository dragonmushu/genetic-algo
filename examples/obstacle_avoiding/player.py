from examples.obstacle_avoiding.game_object import GameObject
from examples.obstacle_avoiding.obstace_avoid_constants import *


class Player(GameObject):
    def __init__(self, pointer_angles, pointer_lengths, speeds, directions):
        GameObject.__init__(self, int(FRAME_WIDTH / 2 - PLAYER_WIDTH / 2), FRAME_HEIGHT - PLAYER_HEIGHT,
                            int(FRAME_WIDTH / 2 - PLAYER_WIDTH / 2) + PLAYER_WIDTH, FRAME_HEIGHT)
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
