from examples.obstacle_avoiding.obstace_avoid_constants import *


class Player:
    def __init__(self, feeler_angles, feeler_lengths, speeds, directions):
        self.current_x = int(FRAME_WIDTH / 2 - PLAYER_WIDTH / 2)
        self.current_y = FRAME_HEIGHT - PLAYER_HEIGHT
        self.feeler_angle_1 = feeler_angles[0]
        self.feeler_angle_2 = feeler_angles[1]
        self.feeler_angle_3 = feeler_angles[2]
        self.feeler_length_1 = feeler_lengths[0]
        self.feeler_length_2 = feeler_lengths[1]
        self.feeler_length_3 = feeler_lengths[2]
        self.speed_1 = speeds[0]
        self.speed_2 = speeds[1]
        self.speed_3 = speeds[2]