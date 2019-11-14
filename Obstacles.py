import game_framework
from pico2d import *

import game_world
import random
import main_state


class JumpObstacle1:
    image = None

    def __init__(self):
        if self.image is None:
            self.image = load_image('jumpObstacle1.png')
        self.frame = 0
        self.x = 400
        self.y = 170
        self.scrollSpeed = 300

    def get_bb(self):
        return self.x - 5, self.y - 50, self.x + 5, self.y - 30

    def update(self):
        self.x -= main_state.scrollspeed * game_framework.frame_time
        if self.x < 0:
            self.x += 2000

    def draw(self):
        self.image.draw(self.x, self.y, 80, 100)
        draw_rectangle(*self.get_bb())


class SlideObstacle1:
    image = None

    def __init__(self):
        if self.image is None:
            self.image = load_image('slideObstacle1.png')
        self.frame = 0
        self.x = 1200
        self.y = 500
        self.scrollSpeed = 300

    def get_bb(self):
        return self.x - 40, self.y - 300, self.x + 40, self.y + 300

    def update(self):
        self.x -= main_state.scrollspeed * game_framework.frame_time
        if self.x < 0:
            self.x += 2000

    def draw(self):
        self.image.draw(self.x, self.y, 80, 600)
        # draw_rectangle(*self.get_bb())


class JumpObstacle2:
    image = None

    def __init__(self):
        if self.image is None:
            self.image = load_image('jumpObstacle2.png')
        self.frame = 0
        self.x = 1500
        self.y = 220
        self.scrollSpeed = 300

    def get_bb(self):
        return self.x - 20, self.y - 100, self.x + 20, self.y - 60

    def update(self):
        self.x -= main_state.scrollspeed * game_framework.frame_time
        if self.x < 0:
            self.x += 2000

    def draw(self):
        self.image.draw(self.x, self.y, 120, 200)
        draw_rectangle(*self.get_bb())


class SlideObstacle2:
    image = None

    def __init__(self):
        if self.image is None:
            self.image = load_image('slideObstacle2.png')
        self.frame = 0
        self.x = 1600
        self.y = 500
        self.scrollSpeed = 300

    def get_bb(self):
        return self.x - 60, self.y - 300, self.x + 60, self.y + 300

    def update(self):
        self.x -= main_state.scrollspeed * game_framework.frame_time
        if self.x < 0:
            self.x += 2000

    def draw(self):
        self.image.draw(self.x, self.y, 120, 600)
        draw_rectangle(*self.get_bb())