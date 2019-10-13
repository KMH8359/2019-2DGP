from pico2d import *

open_canvas()
map = load_image('Map_OVEN1.png')
#if cookienum == 1:
#character = load_image('BraveCookie.png')
#elif cookienum == 2:
#character = load_image('ButtercreamCookie.png')
#elif cookienum == 3:
character = load_image('AngelCookie.png')
#elif cookienum == 4:
#character = load_image('KnightCookie.png')
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
    global stateframeY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            if jumping == False:
                jumping = True
                stateframeY = 10
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            if sliding == False:
                sliding = True
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
    if jumping == True:
        frame = (frame + 1) % 4
    x += 5
    if jumping == True:
        if jumpcount < 4:
            y += 25
            jumpcount += 1
        if jumpcount >= 4:
            y -= 25
            jumpcount += 1
        if jumpcount >= 8:
            jumpcount = 0
            jumping = False
            stateframeY = 1300
    delay(0.05)

close_canvas()
