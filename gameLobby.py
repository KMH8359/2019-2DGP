import game_framework
from pico2d import *
import shop_state
import character_shop_state

name = "gameLobby"
image = None
bgm = None
clickSound = None

point = 100000
font = None

def enter():
    global image
    global font
    global bgm
    global clickSound
    image = load_image('gameLobby.png')
    font = load_font('CookieRunFont.ttf', 27)
    bgm = load_music('Bgm_lobby.ogg')
    clickSound = load_wav('clickSound.wav')
    bgm.set_volume(64)
    clickSound.set_volume(64)
    bgm.repeat_play()

def exit():
    global image
    del image


mouseX, mouseY = 0, 0



def handle_events():
    global mouseX, mouseY
    global clickSound
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            mouseX, mouseY = event.x, 800 - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if 700 <= mouseX <= 1000 and 0 <= mouseY < 150:
                game_framework.change_state(shop_state)
                clickSound.play()
            elif 800 <= mouseX <= 900 and 155 <= mouseY < 235:
                game_framework.change_state(character_shop_state)
                clickSound.play()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
           # elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            #    game_framework.change_state(main_state)


def draw():
    image.draw(600, 400, 1200, 800)
    font.draw(520, 760, ' %5d ' % point, (255, 0, 0))


def update():
    pass


def pause():
    pass


def resume():
    pass
