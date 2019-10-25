from pico2d import *
import game_framework
import json
import os

open_canvas()
map = load_image('Map_OVEN1.png')
#if cookienum == 1:
#character = load_image('BraveCookie.png')
#elif cookienum == 2:
#character = load_image('ButtercreamCookie.png')
#elif cookienum == 3:
#character = load_image('AngelCookie.png')
#elif cookienum == 4:
character = load_image('KnightCookie.png')
#character = load_image('ZombieCookie.png')

running = True
jumping = False
sliding = False
x = 0
y = 0
stateframeY = 1300
frame = 0
cookienum = 2
jumpcount = 0


def handle_events():
    global running
    global cookienum
    global y
    global jumping
    global sliding
    global stateframeY
    global frame
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            if jumping == False and sliding == False:
                jumping = True
                stateframeY = 10
                frame = 0
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            if sliding == False:
                sliding = True
                frame = 8
                stateframeY = 1620
        elif event.type == SDL_KEYUP and event.key == SDLK_DOWN:
            if sliding == True:
                sliding = False
                frame = 0
                stateframeY = 1300
        elif event.type == SDL_MOUSEBUTTONDOWN:
            cookienum += 1
            if cookienum > 4:
                cookienum = 1


while True:
        
    clear_canvas()
    map.draw(400, 300)
    #if cookienum == 1:
    #character.clip_draw(frame * 272 + 10, 1090, 250, 250, x, 200)
    #if cookienum == 2 and cookienum == 3 and cookienum == 4:
    character.clip_draw(frame * 322 + 10, stateframeY , 300, 300, x, 200 + y)
    update_canvas()

    handle_events()
    if jumping == False:
        frame = (frame + 1) % 4
    x += 10
    if jumping == True:
        if jumpcount == 8:
            frame += 1
        if jumpcount == 12:
            frame += 1
        if jumpcount < 10:
            y += 10
            jumpcount += 1
        if jumpcount >= 10:
            y -= 10
            jumpcount += 1
        if jumpcount >= 20:
            jumpcount = 0
            jumping = False
            stateframeY = 1300
    if sliding == True:
        frame = ( frame + 1 ) % 2 + 8
        
    delay(0.05)

close_canvas()

