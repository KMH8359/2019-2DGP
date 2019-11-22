import game_framework
from pico2d import *
import gameLobby

name = "TitleState"
image = None
font = None

def enter():
    global image
    global font
    image = load_image('INTROIMAGE.png')
    font = load_font('CookieRunFont.ttf', 60)

def exit():
    global image
    del image





def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(gameLobby)


def draw():
    image.draw(600, 400, 1200, 800)
    font.draw(300, 200, 'Press Space to Start', (0, 255, 0))


def update():
    pass


def pause():
    pass


def resume():
    pass
