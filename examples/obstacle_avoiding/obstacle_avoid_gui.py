import tkinter as tk
from examples.obstacle_avoiding.obstacle_avoid import *


def setup_window():
    window = tk.Tk()
    window.title('Obstacle Avoiding')
    return window


def setup_frame(window):
    frame = tk.Canvas(window, width=FRAME_WIDTH, height=FRAME_HEIGHT, background="white")
    frame.pack()
    return frame


def run_main_loop(window):
    delta = 0
    while True:
        start_time = time.time()
        print(delta)
        window.update_idletasks()
        window.update()
        delta = time.time() - start_time
        time.sleep(TIME_GAP_IN_SECONDS - delta)
        delta = time.time() - start_time


if __name__ == '__main__':
    window = setup_window()
    frame = setup_frame(window)
    run_main_loop(window)
