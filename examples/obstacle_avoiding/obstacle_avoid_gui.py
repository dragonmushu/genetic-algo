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


def setup_obstacles(frame, obstacles, gui_objects):
    add_new_obstacle_to_list(obstacles)
    new_obstacle_object = create_rectangle_object(frame, obstacles[-1])
    add_gui_object(obstacles[-1], new_obstacle_object, gui_objects)


def update_gui_objects(frame, gui_objects):
    for game_object, gui_object in gui_objects.items():
        frame.move(gui_object, *game_object.delta_position())


def create_rectangle_object(frame, game_object):
    return frame.create_rectangle(*game_object.current_location())


def add_gui_object(game_object, gui_object, gui_objects):
    gui_objects[game_object] = gui_object


def run_main_loop(window, frame):
    delta = 0
    obstacle_addition_delta = 0
    obstacles = []
    gui_objects = {}

    #  initial setup of obstacles
    setup_obstacles(frame, obstacles, gui_objects)

    # initial setup of players

    while True:
        start_time = time.time()

        # update obstacles
        update_all_obstacles(obstacles, delta)


        # update window and frame
        update_gui_objects(frame, gui_objects)
        window.update_idletasks()
        window.update()

        # update game thread
        # print(delta)
        delta = time.time() - start_time
        time.sleep(TIME_GAP_IN_SECONDS - delta)
        delta = time.time() - start_time


if __name__ == '__main__':
    window = setup_window()
    frame = setup_frame(window)
    o1 = Obstacle()
    run_main_loop(window, frame)
