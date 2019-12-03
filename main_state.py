from pico2d import *
import game_framework
import game_world
import json
import os
import title_state
import random
import gameLobby
import gameEnd
import shop_state
import character_shop_state

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
point = 0
eat_sound = None



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
    jellies = [YellowBear() for i in range(35)] + [PinkBear() for i in range(33)]
    for i in range(68):
        jellies[i].x = 50 * i + 600
        jellies[i].y = 200
    jellies[1].y = 250
    jellies[2].y = 300
    jellies[3].y = 250
    jellies[14].y = 270
    jellies[15].y = 340
    jellies[16].y = 410
    jellies[17].y = 340
    jellies[18].y = 270
    jellies[29].y = 150
    jellies[30].y = 150
    jellies[31].y = 150
    jellies[43].y = 275
    jellies[44].y = 350
    jellies[45].y = 275
    jellies[57].y = 150
    jellies[58].y = 150
    jellies[59].y = 150
    jellies[60].y = 150
    jellies[61].y = 150
    jellies[62].y = 150
    jellies[63].y = 150
    jellies[64].y = 150
    jellies[65].y = 150
    jellies[66].y = 150
    jellies[67].y = 150
    game_world.add_objects(jellies, 3)
    global maptile
    maptile = MapTile()
    game_world.add_object(maptile, 2)
    global obstacles
    obstacles = [JumpObstacle1() for i in range(2)] + [JumpObstacle2() for i in range(2)] + [JumpObstacle3() for i in range(2)] + [SlideObstacle1() for i in range(2)] + [SlideObstacle2() for i in range(2)]
    obstacles[7].x = 3700
    obstacles[9].x = 3900
    obstacles[3].x = 4500
    game_world.add_objects(obstacles, 4)
    global point
    point = 0
    global eat_sound
    eat_sound = load_wav('eat_sound.wav')
    eat_sound.set_volume(48)

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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_3:
            character.image = load_image('ButterCreamCookie.png')
        elif event.type == SDL_KEYDOWN and event.key == SDLK_1:
            character.image = load_image('BrightCookie.png')
        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
            character.image = load_image('CloudCookie.png')
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
        if character.DEATHCOUNT > 200:
            game_world.remove_object(character)
            for jelly in jellies:
                game_world.remove_object(jelly)
            for ITEM in items:
                game_world.remove_object(ITEM)
            for obstacle in obstacles:
                game_world.remove_object(obstacle)
            game_world.remove_object(maptile)
            hpBar.bgm.stop()
            game_world.remove_object(hpBar)
            game_world.remove_object(Background)
            game_framework.change_state(gameEnd)

    for jelly in jellies:
        if collide(character, jelly):
            jelly.x += 5000
            character.score += (100 + shop_state.JellyValue)
            eat_sound.play()
            # jellies.remove(jelly)
            # game_world.remove_object(jelly)
    for ITEM in items:
        if collide(character, ITEM):
            if ITEM.type == 'Faster':
                if character_shop_state.CloudCookieSelected:
                    runTimer = 6.5
                else:
                    runTimer = 5
                scrollspeed = 1000
                character.running = True
            elif ITEM.type == 'Bigger':
                if character_shop_state.CloudCookieSelected:
                    bigTimer = 6.5
                else:
                    bigTimer = 5
                character.bigger = True
            elif ITEM.type == 'smallHP':
                character.HP += 50
                hpBar.w += 100
            ITEM.x += 10000
    for obstacle in obstacles:
        if collide(character, obstacle):
            if character.invincible <= 0:
                character.HP -= 300
                hpBar.w -= 600
                character.invincible = 2


def draw():
    for game_object in game_world.all_objects():
        game_object.draw()
