import game_framework
from pico2d import *

import game_world
import random
import main_state

class YellowBear:
    image = None

    def __init__(self):
        if self.image is None:
            self.image = load_image('YellowJellies.png')
        self.frame = 0
        self.scrollSpeed = 300

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def update(self):
        self.x -= main_state.scrollspeed * game_framework.frame_time
        if self.x < 0:
            self.x += 2000

    def draw(self):
        self.image.clip_draw(self.frame * 57, 0, 57, 50, self.x, self.y, 50, 50)
        # draw_rectangle(*self.get_bb())


class PinkBear:
    image = None

    def __init__(self):
        if self.image is None:
            self.image = load_image('PinkJellies.png')
        self.frame = 0
        self.scrollSpeed = 300

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def update(self):
        self.x -= main_state.scrollspeed * game_framework.frame_time
        if self.x < 0:
            self.x += 2000

    def draw(self):
        self.image.clip_draw(self.frame * 57, 0, 57, 50, self.x, self.y, 50, 50)
        # draw_rectangle(*self.get_bb())
