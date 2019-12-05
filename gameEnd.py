import game_framework
from pico2d import *
import gameLobby
import main_state

name = "gameEnd"
image = None
score_count_sound = None
font = None

def enter():
    global image
    global font
    global score_count_sound
    image = load_image('gameEnd.png')
    font = load_font('CookieRunFont.ttf', 100)
    score_count_sound = load_wav('score_count_sound.wav')
    score_count_sound.set_volume(96)
    score_count_sound.play()

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
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if 470 <= mouseX <= 720 and 40 <= mouseY < 140:
                gameLobby.bgm.repeat_play()
                game_framework.change_state(gameLobby)
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
           # elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            #    game_framework.change_state(main_state)


def draw():
    image.draw(600, 400, 1200, 800)
    font.draw(400, 390, ' %5d ' % main_state.point, (255, 0, 0))


def update():
    pass


def pause():
    pass


def resume():
    pass
