import tkinter as tk
from examples.obstacle_avoiding.obstacle_avoid import *


def setup_frame():
    window = tk.Tk()
    window.title('Obstacle Avoiding')
    frame = tk.Canvas(window, width=FRAME_WIDTH, height=FRAME_HEIGHT, background="white")
    frame.pack()
    frame.create_rectangle(*random_rectangle_at_top(), fill="red", outline="red")
    frame.create_rectangle(*initial_player_location(), fill="red", outline="red")
    window.mainloop()


if __name__ == '__main__':
    setup_frame()
