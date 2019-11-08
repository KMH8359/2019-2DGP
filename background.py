import random

from pico2d import *

import game_world
import game_framework


class InfiniteBackground:

    def __init__(self):
        self.image = load_image('Map_OVEN1.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def set_center_object(self, boy):
        self.center_object = boy

    def draw(self):
        self.image.clip_draw_to_origin(self.q3l, self.q3b, self.q3w, self.q3h, 0, 0)
        self.image.clip_draw_to_origin(self.q2l, self.q2b, self.q2w, self.q2h, 0, self.q3h)
        self.image.clip_draw_to_origin(self.q4l, self.q4b, self.q4w, self.q4h, self.q3w, 0)
        self.image.clip_draw_to_origin(self.q1l, self.q1b, self.q1w, self.q1h, self.q3w, self.q3h)  # quadrant 3

    def update(self):
        # quadrant 3
        self.q3l = (int(self.center_object.x) - self.canvas_width // 8) % self.w
        self.q3b = (int(self.center_object.y) - self.canvas_height // 8) % self.h
        self.q3w = clamp(0, self.w - self.q3l, self.w)
        self.q3h = clamp(0, self.h - self.q3b, self.h)

        # quadrant 2
        self.q2l = self.q3l
        self.q2b = 0
        self.q2w = self.q3w
        self.q2h = self.canvas_height - self.q3h

        # quadrand 4
        self.q4l = 0
        self.q4b = self.q3b
        self.q4w = self.canvas_width - self.q3w
        self.q4h = self.q3h

        # quadrand 1
        self.q1l = 0
        self.q1b = 0
        self.q1w = self.q4w
        self.q1h = self.q2h

    def handle_event(self, event):
        pass


class MapTile:
    image = None

    def __init__(self):
        self.image = load_image('maptiles.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.tiles = [n for n in range(11)]
        self.x = 600
        self.X = 1800
        # self.tiles = [-62, 62, 186, 310,

    def set_center_object(self, boy):
        self.center_object = boy

    def draw(self):
        # for i in range(0, 11):
        #   self.image.draw(-62 + self.window_left + 124 * i,60)
        self.image.draw(self.x, 60)
        self.image.draw(self.X, 60)

    def get_bb(self):
        return self.x - 25, self.y + 100, self.x + 150, self.y + 120

    def update(self):
        pass
        self.window_left = clamp(0,
                                 int(self.center_object.x) - self.canvas_width // 4,
                                 self.w - self.canvas_width)
        self.x -= 2
        self.X -= 2
        if self.x < -600:
            self.x = 1800
        if self.X < -600:
            self.X = 1800

        self.window_bottom = 0

    def handle_event(self, event):
        pass
