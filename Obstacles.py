import game_framework
from pico2d import *

import game_world
import random

class JumpObstacle:
    image = None
    def __init__(self):
        self.image = load_image('jumpObstacle1.png')
        self.frame = 0
        self.x = 400
        self.y = 170
    def get_bb(self):
        return self.x - 5, self.y - 50, self.x + 5, self.y - 30
    def update(self):
        self.x -= 2
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
        self.x = 1200
        self.y = 500
    def get_bb(self):
        return self.x - 40, self.y - 300, self.x + 40, self.y + 300
    def update(self):
        self.x -= 2
        if self.x < 0:
            self.x = 2000
    def draw(self):
        self.image.draw(self.x,self.y,80,600)
        draw_rectangle(*self.get_bb())
