import tkinter as tk
from examples.obstacle_avoiding.obstacle_avoid import *


# setup functions
def setup_window():
    window = tk.Tk()
    window.title('Obstacle Avoiding')
    return window


def setup_frame(window):
    frame = tk.Canvas(window, width=FRAME_WIDTH, height=FRAME_HEIGHT, background="white")
    frame.pack()
    return frame


# update functions
def update_gui_objects(frame, gui_objects):
    for gui_object in gui_objects:
        gui_object.update_gui_object(frame)


if __name__ == '__main__':
    window = setup_window()
    frame = setup_frame(window)
    run_main_loop(window, frame)
