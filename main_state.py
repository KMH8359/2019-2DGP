from pico2d import *
import game_framework
import json
import os
import title_state
import random

#import shop_state
#map = load_image('Map_OVEN1.png')
#character = load_image('BraveCookie.png')
cookienum = 1
#cookienum = 2
#character = load_image('ButtercreamCookie.png')
#character = load_image('AngelCookie.png')
#character = load_image('KnightCookie.png')
#character = load_image('ZombieCookie.png')

name = "MainState"

map = None
character = None
bigcoin = None
bigger = None
drain = None
faster = None
smallhp = None

class Character:
    def __init__(self):
        if cookienum == 1:
            self.image = load_image('BraveCookie.png')
        self.x = 0
        self.y = 0
        self.frameX = 0
        self.running = True
        self.jumping = False
        self.sliding = False
        self.frameY = 1090
        self.jumpcount = 0
    def update(self):
        if self.running == True:
            self.frameX = (self.frameX + 1 )  % 4
            
        elif self.jumping == True:
            self.frameX = (self.frameX + 1) % 2 + 7
            if self.jumpcount == 30:
                self.frameX += 1
            if self.jumpcount == 60:
                self.frameX += 1
            if self.jumpcount < 100:
                self.y += 1
                self.jumpcount += 1
            if self.jumpcount >= 100:
                self.y -= 1
                self.jumpcount += 1
            if self.jumpcount >= 200:
                self.jumpcount = 0
                self.jumping = False
                self.running = True
                self.frameY = 1090
                
        elif self.sliding == True:
            self.frameX = (self.frameX + 1 ) % 2 + 9           
        self.x += 1
    def draw(self):
        self.image.clip_draw((self.frameX) * 272 + 10, self.frameY, 250, 250, self.x, 200 + self.y,200,200)

class Coin:
    def __init__(self):
        self.image = load_image('BigCoin.png')
    def draw(self):
        self.image.clip_draw(0,0,160,160,random.randint(0,800),random.randint(0,600),50,50)
class Bigger:
    def __init__(self):
        self.image = load_image('Bigger.png')
    def draw(self):
        self.image.clip_draw(0,0,90,90,random.randint(0,800),random.randint(0,600),50,50)
class Drain:
    def __init__(self):
        self.image = load_image('drain.png')
    def draw(self):
        self.image.clip_draw(0,0,90,90,random.randint(0,800),random.randint(0,600),50,50)
class Faster:
    def __init__(self):
        self.image = load_image('Faster.png')
    def draw(self):
        self.image.clip_draw(0,0,90,90,random.randint(0,800),random.randint(0,600),50,50)
class smallHP:
    def __init__(self):
        self.image = load_image('smallHP.png')
    def draw(self):
        self.image.clip_draw(0,0,90,90,random.randint(0,800),random.randint(0,600),50,50)

class Map:
    def __init__(self):
        self.image = load_image('Map_OVEN1.png')
    def draw(self):
        self.image.draw(400,300,800,600)

def enter():
    global character,map,bigcoin,bigger,drain,faster,smallhp
    character = Character()
    map = Map()
    bigcoin = Coin()
    bigger = Bigger()
    drain = Drain()
    faster = Faster()
    smallhp = smallHP()
    #items = [Item() for i in range(100)]
def exit():
    global character, map,bigcoin,bigger,drain,faster,smallhp
    del(character)
    del(map)
    del(bigcoin)
    del(bigger)
    del(drain)
    del(faster)
    del(smallhp)


def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            character.running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            character.running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            if character.jumping == False and character.sliding == False:
                character.jumping = True
                character.running = False
                character.frameX = 0
                character.frameY = 1360
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            if character.sliding == False and character.jumping == False:
                character.sliding = True
                character.running = False
                character.frameX = 0
                character.frameY = 1360
        elif event.type == SDL_KEYUP and event.key == SDLK_DOWN:
            if character.sliding == True:
                character.sliding = False
                character.running = True
                character.frameX = 0
                character.frameY = 1090
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
            game_framework.change_state(shop_state)
    
def update():
    character.update()
    
def draw():
    map.draw()
    character.draw()
    bigcoin.draw()
    bigger.draw()
    drain.draw()
    faster.draw()
    smallhp.draw()
        



