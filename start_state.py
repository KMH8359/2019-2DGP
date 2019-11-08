import game_framework
from pico2d import *

name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('kpu_credit.png')


def exit():
    global image
    del image


import title_state


def update():
    global logo_time

    if logo_time > 1.0:
        logo_time = 0
        # game_framework.quit()
        game_framework.change_state(title_state)
    delay(0.01)
    logo_time += 0.01


def draw():
    global image
    image.draw(600, 400, 1200, 800)


def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass
