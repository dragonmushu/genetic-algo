PLAYER_WIDTH = 10
PLAYER_HEIGHT = 10

FRAME_WIDTH = 400
FRAME_HEIGHT = 600
FPS = 30  # 30 frames per second
TIME_GAP_IN_SECONDS = 1/FPS  # gap between successive frames in seconds

OBSTACLE_WIDTH = 80
OBSTACLE_HEIGHT = 10
OBSTACLE_SPEED = 5  # pixels per second
OBSTACLE_ADDITION_PERIOD =  4  # seconds between obstacle addition

PLAYER_CHROMOSOME_LENGTH = 48
'''
Genetic Algorithm Explanation:

A box tries to avoid obstacles that falls down on it
The box has three pointers that allow it to move accordingly
The pointers can have varying angles from (1, 180) and lengths from (5, 20) px
If the pointer is activated the box will move in a certain direction

angle: 180 (8 bits) int(val/255*180)
length: 5-20 (4 bits) int(val/15*11) + 5
speed: 0-7 (3 bits)
direction: 0-1 (1 bit)

3 pointers: 3*(8 + 4 + 3 + 1) = 48
Player dies when an obstacle hits it
'''

