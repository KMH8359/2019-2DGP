from pico2d import *

open_canvas()
map = load_image('Map_OVEN1.png')
#if cookienum == 1:
#character = load_image('BraveCookie.png')
#elif cookienum == 2:
character = load_image('ButtercreamCookie.png')
#elif cookienum == 3:
#character = load_image('AngelCookie.png')
#elif cookienum == 4:
#character = load_image('KnightCookie.png')

running = True
x = 0
frame = 0
cookienum = 2


def handle_events():
    global running
    global cookienum
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
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
    character.clip_draw(frame * 322 + 10, 1300, 300, 300, x, 200)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 4
    x += 5
    delay(0.05)

close_canvas()

