import random

from pico2d import *

import game_world
import game_framework

class MapTile:
    image = None
    def __init__(self):
        self.image = load_image('mapTile.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        
    def set_center_object(self, boy):
        self.center_object = boy
        
    def draw(self):
        for i in range(1, int(self.image_frame)):
            self.image.clip_draw_to_origin(
            self.window_left + i * 120, self.window_bottom,
            120, 120, 0, 0)
    def get_bb(self):
        return self.x - 25, self.y + 100, self.x + 150, self.y + 120
    
    def update(self):
        pass
        self.window_left = clamp(0,
            int(self.center_object.x) - self.canvas_width//2,
            self.w - self.canvas_width)
        self.window_bottom = 0
        self.image_frame = (self.window_left + self.canvas_width) / 120

    def handle_event(self, event):
        pass





