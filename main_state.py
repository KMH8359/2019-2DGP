from pico2d import *
import game_framework
import game_world
import json
import os
import title_state
import random

from character import Character
from background import FixedBackground as Background

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


class Coin:
    global character
    def __init__(self):
        self.image = load_image('BigCoin.png')
        self.frame = 0
        self.x = 100
        self.y = 200
    def update(self):
        self.frame = (self.frame + 1) % 4
        if self.x <= character.x + 250 and self.x + 50 >= character.x and self.y <= character.y + 250 and self.y + 50 >= character.y:
            del(self)
    def draw(self):
        self.image.clip_draw(self.frame,0,160,160,self.x,self.y,50,50)
class Bigger:
    global character
    def __init__(self):
        self.image = load_image('Bigger.png')
        self.frame = 0
        self.x = 200
        self.y = 200
    def update(self):
        self.frame = (self.frame + 1) % 4
        if self.x <= character.x + 250 and self.x + 50 >= character.x and self.y <= character.y + 250 and self.y + 50 >= character.y:
            del(self)
    def draw(self):
        self.image.clip_draw(self.frame,0,90,90,self.x,self.y,50,50)
class Drain:
    global character
    def __init__(self):
        self.image = load_image('drain.png')
        self.frame = 0
        self.x = 300
        self.y = 200
    def update(self):
        self.frame = (self.frame + 1) % 4
        if self.x <= character.x + 250 and self.x + 50 >= character.x and self.y <= character.y + 250 and self.y + 50 >= character.y:
            del(self)
    def draw(self):
        self.image.clip_draw(self.frame,0,90,90,self.x,self.y,50,50)
class Faster:
    global character
    def __init__(self):
        self.image = load_image('Faster.png')
        self.frame = 0
        self.x = 400
        self.y = 200
    def update(self):
        self.frame = (self.frame + 1) % 4
        if self.x <= character.x + 250 and self.x + 50 >= character.x and self.y <= character.y + 250 and self.y + 50 >= character.y:
            del(self)
    def draw(self):
        self.image.clip_draw(self.frame,0,90,90,self.x,self.y,50,50)
class smallHP:
    global character
    def __init__(self):
        self.image = load_image('smallHP.png')
        self.frame = 0
        self.x = 500
        self.y = 200
    def update(self):
        self.frame = (self.frame + 1) % 4
        if self.x <= character.x + 250 and self.x + 50 >= character.x and self.y <= character.y + 250 and self.y + 50 >= character.y:
            del(self)
    def draw(self):
        self.image.clip_draw(self.frame,0,90,90,self.x,self.y,50,50)

class Map:
    def __init__(self):
        self.image = load_image('Map_OVEN1.png')
    def draw(self):
        self.image.draw(400,300,800,600)

def enter():
    global character
    character = Character()
    game_world.add_object(character, 1)
    #global map
    #map = Map()
    global background
    background = Background()
    game_world.add_object(background, 0)
    global bigcoin
    bigcoin = Coin()
    game_world.add_object(bigcoin, 2)
    global bigger
    bigger = Bigger()
    game_world.add_object(bigger, 3)
    global drain
    drain = Drain()
    game_world.add_object(drain, 4)
    global faster
    faster = Faster()
    game_world.add_object(faster, 5)
    global smallhp
    smallhp = smallHP()
    game_world.add_object(smallhp, 6)
    background.set_center_object(character)
    character.set_background(background)
def exit():
    #global character, map,bigcoin,bigger,drain,faster,smallhp
    #del(character)
    #del(map)
    #del(bigcoin)
    #del(bigger)
    #del(drain)
    #del(faster)
    #del(smallhp)
    game_world.clear()


def pause():
    pass

def resume():
    pass

def handle_events():
    global character
    global cookienum
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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
            cookienum = 2
            del(character)
            character = Character()
        elif event.type == SDL_KEYUP and event.key == SDLK_DOWN:
            if character.sliding == True:
                character.sliding = False
                character.running = True
                character.frameX = 0
                character.frameY = 1090
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
            game_framework.change_state(shop_state)
    
def update():
    for game_object in game_world.all_objects():
        game_object.update()
    #character.update()
    #bigcoin.update()
    #bigger.update()
    #drain.update()
    #faster.update()
    #smallhp.update()
    
def draw():
    #background.draw()
    #character.draw()
    for game_object in game_world.all_objects():
        game_object.draw()
    #bigcoin.draw()
    #bigger.draw()
    #drain.draw()
    #faster.draw()
    #smallhp.draw()
        



