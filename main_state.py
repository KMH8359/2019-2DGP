from pico2d import *
import game_framework
import game_world
import json
import os
import title_state
import random

from character import Character
#from background import FixedBackground as Background
from background import InfiniteBackground as Background
from item import Coin, Bigger, Drain, Faster, smallHP
from background import MapTile

name = "MainState"

map = None
character = None
maptile = None
items = []


def enter():
    global character
    character = Character()
    game_world.add_object(character, 1)
    global background
    background = Background()
    game_world.add_object(background, 0)
    global items
    items = [Coin() for i in range(10)] + [Bigger() for i in range(10)] + [Drain() for i in range(10)] + [Faster() for i in range(10)] + [smallHP() for i in range(10)]
    game_world.add_objects(items, 1)
    global maptile
    maptile = MapTile()
    game_world.add_object(maptile, 2)
    
    background.set_center_object(character)
    maptile.set_center_object(character)
    character.set_background(background)
def exit():
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
    
def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True
def pause():
    pass

def resume():
    pass

def update():
    for game_object in game_world.all_objects():
        game_object.update()
    for bigger in items:
        if collide(character, bigger):
            items.remove(bigger)
            game_world.remove_object(bigger)
    for faster in items:
        if collide(character, faster):
            items.remove(faster)
            game_world.remove_object(faster)
    
def draw():
    for game_object in game_world.all_objects():
        game_object.draw()
        



