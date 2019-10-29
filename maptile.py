import random

from pico2d import *

import game_world
import game_framework

class MapTile:
    image = None
    def __init__(self):
        self.image = load_image('maptile.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.x = 600
        self.2x = 1800
        
    def set_center_object(self, boy):
        self.center_object = boy
        
    def draw(self):
        #for i in range(1, int(self.image_frame)):
         #   self.image.clip_draw_to_origin(
          #  self.window_left + i * 120, self.window_bottom,
           # 120, 120, 0, 0)
        self.image_draw(self.x,60,1200,120)
        self.image_draw(self.2x,60,1200,120)
        
    def get_bb(self):
        return self.x - 25, self.y + 100, self.x + 150, self.y + 120
    
    def update(self):
        pass
        self.window_left = clamp(0,
            int(self.center_object.x) - self.canvas_width//2,
            self.w - self.canvas_width)
        self.window_bottom = 0
        self.image_frame = (self.window_left + self.canvas_width) / 120
        self.x -= 5
        self.2x -= 5
        if self.x < -600:
            self.x = 1800
        if self.2x < -600:
            self.2x = 1800

    def handle_event(self, event):
        pass





