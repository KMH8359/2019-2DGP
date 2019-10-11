from pico2d import *

open_canvas()
map = load_image('Map_OVEN1.png')
character = load_image('BraveCookie.png')


running = True
x = 0
frame = 0


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


while True:
    clear_canvas()
    map.draw(400, 300)
    character.clip_draw(frame * 272 + 10, 1090, 250, 250, x, 200)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 4
    x += 5
    delay(0.05)

close_canvas()

