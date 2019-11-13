import game_framework
from pico2d import *

import game_world
import random
import main_state

class Coin:
    image = None

    def __init__(self):
        if self.image is None:
            self.image = load_image('BigCoin.png')
        self.frame = 0
        self.x = 1900
        self.y = 300

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 75, self.y + 75

    def update(self):
        self.frame = (self.frame + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame, 0, 160, 160, self.x, self.y, 50, 50)


class Bigger:
    image = None

    def __init__(self):
        if self.image is None:
            self.image = load_image('Bigger.png')
        self.frame = 0
        self.x = 1900
        self.y = 350
        self.type = "Bigger"
        self.scrollSpeed = 300

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def update(self):
        self.x -= main_state.scrollspeed * game_framework.frame_time
        if self.x < 0:
            self.x += 2000

    def draw(self):
        self.image.clip_draw(self.frame, 0, 90, 90, self.x, self.y, 75, 75)
        draw_rectangle(*self.get_bb())


class Drain:
    image = None

    def __init__(self):
        if self.image is None:
            self.image = load_image('drain.png')
        self.frame = 0
        self.x = 1900
        self.y = 300

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 75, self.y + 75

    def update(self):
        self.frame = (self.frame + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame, 0, 90, 90, self.x, self.y, 50, 50)


class Faster:
    image = None

    def __init__(self):
        if self.image is None:
            self.image = load_image('Faster.png')
        self.frame = 0
        self.x = 2000
        self.y = 350
        self.scrollSpeed = 300
        self.type = 'Faster'

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def update(self):
        self.x -= main_state.scrollspeed * game_framework.frame_time
        if self.x < 0:
            self.x += 2000

    def draw(self):
        self.image.clip_draw(self.frame, 0, 90, 90, self.x, self.y, 75, 75)
        draw_rectangle(*self.get_bb())


class smallHP:
    image = None

    def __init__(self):
        self.image = load_image('smallHP.png')
        self.frame = 0
        self.x = 1900
        self.y = 300

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 75, self.y + 75

    def update(self):
        self.frame = (self.frame + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame, 0, 90, 90, self.x, self.y, 50, 50)
