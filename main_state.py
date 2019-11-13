from pico2d import *
import game_framework
import game_world
import json
import os
import title_state
import random

from character import Character, WalkingState, RunningState, SPACE, LSHIFT
from background import InfiniteBackground as Background
from item import Coin, Bigger, Drain, Faster, smallHP
from background import MapTile
from Jellies import PinkBear, YellowBear
from Obstacles import JumpObstacle, SlideObstacle

name = "MainState"

map = None
character = None
maptile = None
items = []
jellies = []
jumpobstacles = []
slideobstacles = []
scrollspeed = 500
runTimer = 0

def enter():
    global character
    character = Character()
    game_world.add_object(character, 1)
    global background
    background = Background()
    game_world.add_object(background, 0)
    global items
    items = [Bigger() for i in range(3)] + [Faster() for i in range(3)]
    game_world.add_objects(items, 1)
    global jellies
    jellies = [YellowBear() for i in range(15)] + [PinkBear() for i in range(15)]
    for i in range(30):
        jellies[i].x = 50 * i + 300
        jellies[i].y = 200
    jellies[1].y = 250
    jellies[2].y = 300
    jellies[3].y = 250
    jellies[17].y = 150
    jellies[18].y = 150
    jellies[19].y = 150
    game_world.add_objects(jellies, 3)
    global maptile
    maptile = MapTile()
    game_world.add_object(maptile, 2)
    global jumpobstacles
    jumpobstacles = JumpObstacle()
    game_world.add_object(jumpobstacles, 4)
    global slideobstacles
    slideobstacles = SlideObstacle()
    game_world.add_object(slideobstacles, 4)

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
    global scrollspeed
    global runTimer
    if runTimer > 0:
        runTimer -= game_framework.frame_time
    if runTimer < 0:
        character.cur_state = WalkingState
        character.cur_state.enter(character, None)
        scrollspeed = 500
        runTimer = 0
    if character.HP > 0:
        for game_object in game_world.all_objects():
            game_object.update()
    else:
        character.update()
    for jelly in jellies:
        if collide(character, jelly):
            jelly.x += 2000
            character.score += 100
            # jellies.remove(jelly)
            # game_world.remove_object(jelly)
    for ITEM in items:
        if collide(character, ITEM):
            if ITEM.type == 'Faster':
                runTimer = 5
                scrollspeed = 1000
                character.cur_state = RunningState
                character.cur_state.enter(character, None)
            elif ITEM.type == 'Bigger':
                pass
            ITEM.x += 2000
    if collide(character, jumpobstacles) or collide(character, slideobstacles):
        if character.invincible == 0:
            # character.HP -= 50
            print(character.HP)
            character.invincible += 500

def draw():
    for game_object in game_world.all_objects():
        game_object.draw()
