from pico2d import *
import game_framework
import game_world
import json
import os
import title_state
import random

from character import Character
from background import InfiniteBackground as Background
from item import Coin, Bigger, Drain, Faster, smallHP
from background import MapTile, HPbar
from Jellies import PinkBear, YellowBear
from Obstacles import JumpObstacle1, JumpObstacle2, JumpObstacle3,   SlideObstacle1, SlideObstacle2

name = "MainState"

map = None
character = None
maptile = None
hpBar = None
items = []
jellies = []
obstacles = []
scrollspeed = 500
runTimer = 0
bigTimer = 0


def enter():
    global character
    character = Character()
    game_world.add_object(character, 1)
    global hpBar
    hpBar = HPbar()
    game_world.add_object(hpBar, 1)
    global background
    background = Background()
    game_world.add_object(background, 0)
    global items
    items = [Bigger() for i in range(1)] + [Faster() for i in range(1)] + [smallHP() for i in range(1)]
    game_world.add_objects(items, 1)
    global jellies
    jellies = [YellowBear() for i in range(30)] + [PinkBear() for i in range(30)]
    for i in range(60):
        jellies[i].x = 50 * i + 600
        jellies[i].y = 200
    jellies[1].y = 250
    jellies[2].y = 300
    jellies[3].y = 250
    jellies[6].y = 250
    jellies[7].y = 300
    jellies[8].y = 350
    jellies[9].y = 300
    jellies[10].y = 250
    jellies[22].y = 150
    jellies[23].y = 150
    jellies[24].y = 150
    jellies[25].y = 150
    jellies[26].y = 150
    game_world.add_objects(jellies, 3)
    global maptile
    maptile = MapTile()
    game_world.add_object(maptile, 2)
    global obstacles
    obstacles = [JumpObstacle1() for i in range(2)] + [JumpObstacle2() for i in range(2)] + [JumpObstacle3() for i in range(2)] + [SlideObstacle1() for i in range(2)] + [SlideObstacle2() for i in range(2)]
    game_world.add_objects(obstacles, 4)
    #global jumpobstacles
    #jumpobstacles = [JumpObstacle1() for i in range(2)] + [JumpObstacle2() for i in range(2)]
    #game_world.add_objects(jumpobstacles, 4)
    #global slideobstacles
    #slideobstacles = [SlideObstacle1() for i in range(2)] + [SlideObstacle2() for i in range(2)]
    #game_world.add_objects(slideobstacles, 4)

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
    global bigTimer
    if runTimer > 0:
        runTimer -= game_framework.frame_time
    if runTimer < 0:
        character.running = False
        scrollspeed = 500
        runTimer = 0
    if bigTimer > 0:
        bigTimer -= game_framework.frame_time
    if bigTimer < 0:
        character.bigger = False
        bigTimer = 0
    if character.HP > 0:
        for game_object in game_world.all_objects():
            game_object.update()
    else:
        character.update()
    for jelly in jellies:
        if collide(character, jelly):
            jelly.x += 5000
            character.score += 100
            # jellies.remove(jelly)
            # game_world.remove_object(jelly)
    for ITEM in items:
        if collide(character, ITEM):
            if ITEM.type == 'Faster':
                runTimer = 5
                scrollspeed = 1000
                character.running = True
            elif ITEM.type == 'Bigger':
                bigTimer = 5
                character.bigger = True
            ITEM.x += 15000
    for obstacle in obstacles:
        if collide(character, obstacle):
            if character.invincible == 0:
                character.HP -= 100
                hpBar.w -= 200
                character.invincible += 500


def draw():
    for game_object in game_world.all_objects():
        game_object.draw()
