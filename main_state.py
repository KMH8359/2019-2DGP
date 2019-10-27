from pico2d import *
import game_framework
import game_world
import json
import os
import title_state
import random

from character import Character
from background import FixedBackground as Background
from items import Coin
from items import Bigger
from items import Drain
from items import Faster
from items import smallHP

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

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            character.handle_event(event)
    

def pause():
    pass

def resume():
    pass

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
        



