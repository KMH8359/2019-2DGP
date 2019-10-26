import game_framework
from pico2d import *
import main_state

name = "ShopState"
image = None

def enter():
    global image
    image = load_image
