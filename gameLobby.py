import game_framework
from pico2d import *
import shop_state

name = "gameLobby"
image = None

point = 0
font = None

def enter():
    global image
    global font
    image = load_image('gameLobby.png')
    font = load_font('CookieRunFont.ttf', 36)

def exit():
    global image
    del image


mouseX, mouseY = 0, 0


def handle_events():
    global mouseX, mouseY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            mouseX, mouseY = event.x, 800 - 1 - event.y
            print(mouseX)
            print(mouseY)
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if 700 <= mouseX <= 1000 and 0 <= mouseY < 150:
                game_framework.change_state(shop_state)
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
           # elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            #    game_framework.change_state(main_state)


def draw():
    image.draw(600, 400, 1200, 800)
    font.draw(500, 770, ' %5d ' % point, (255, 0, 0))


def update():
    pass


def pause():
    pass


def resume():
    pass
