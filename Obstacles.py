import game_framework
from pico2d import *

import game_world
import random

class JumpObstacle:
    image = None
    def __init__(self):
        self.image = load_image('jumpObstacle1.png')
        self.frame = 0
        self.x = 800
        self.y = 170
        self.savedx = self.x
        self.savedy = self.y
    def get_bb(self):
        return self.x - 5, self.y - 30, self.x + 5, self.y - 10
    def update(self):
        self.x -= 1
        if self.x < 0:
            self.x = 2000
    def draw(self):
        self.image.draw(self.x,self.y,80,100)
        draw_rectangle(*self.get_bb())
class SlideObstacle:
    image = None
    def __init__(self):
        self.image = load_image('slideObstacle1.png')
        self.frame = 0
        self.x = 1500
        self.y = 320
        self.savedx = self.x
        self.savedy = self.y
    def get_bb(self):
        return self.x, self.y, self.x + 100, self.y + 480
    def update(self):
        self.x -= 1
        if self.x < 0:
            self.x = self.savedx
    def draw(self):
        self.image.draw(self.x,self.y,80,480)
