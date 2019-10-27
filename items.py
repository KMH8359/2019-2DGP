import game_framework
from pico2d import *

import game_world
import random

class Coin:
    def __init__(self):
        self.image = load_image('BigCoin.png')
        self.frame = 0
        self.x = random.randint(0,2000)
        self.y = random.randint(50, 250)
    def update(self):
        self.frame = (self.frame + 1) % 4
    def draw(self):
        self.image.clip_draw(self.frame,0,160,160,self.x,self.y,50,50)
class Bigger:
    def __init__(self):
        self.image = load_image('Bigger.png')
        self.frame = 0
        self.x = random.randint(0,2000)
        self.y = random.randint(50, 250)
    def update(self):
        self.frame = (self.frame + 1) % 4
    def draw(self):
        self.image.clip_draw(self.frame,0,90,90,self.x,self.y,50,50)
class Drain:
    global character
    def __init__(self):
        self.image = load_image('drain.png')
        self.frame = 0
        self.x = random.randint(0,2000)
        self.y = random.randint(50, 250)
    def update(self):
        self.frame = (self.frame + 1) % 4
    def draw(self):
        self.image.clip_draw(self.frame,0,90,90,self.x,self.y,50,50)
class Faster:
    global character
    def __init__(self):
        self.image = load_image('Faster.png')
        self.frame = 0
        self.x = random.randint(0,2000)
        self.y = random.randint(50, 250)
    def update(self):
        self.frame = (self.frame + 1) % 4
    def draw(self):
        self.image.clip_draw(self.frame,0,90,90,self.x,self.y,50,50)
class smallHP:
    global character
    def __init__(self):
        self.image = load_image('smallHP.png')
        self.frame = 0
        self.x = random.randint(0,2000)
        self.y = random.randint(50, 250)
    def update(self):
        self.frame = (self.frame + 1) % 4
    def draw(self):
        self.image.clip_draw(self.frame,0,90,90,self.x,self.y,50,50)
