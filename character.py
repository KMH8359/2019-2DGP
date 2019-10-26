import game_framework
from pico2d import *

import game_world

# Character Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Character Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8



# Character Event
UPKEY_DOWN, DOWNKEY_DOWN,UPKEY_UP, DOWNKEY_UP, SPACE = range(5)

key_event_table = {
    (SDL_KEYDOWN, SDLK_UP): UPKEY_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWNKEY_DOWN,
    (SDL_KEYUP, SDLK_UP): UPKEY_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWNKEY_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


# Character States

class WalkingState:

    @staticmethod
    def enter(character, event):
        if event == UPKEY_DOWN:
            character.y_velocity += RUN_SPEED_PPS
        elif event == UPKEY_UP:
            character.y_velocity -= RUN_SPEED_PPS
        if event == DOWNKEY_DOWN:
            character.y_velocity -= RUN_SPEED_PPS
        elif event == DOWNKEY_UP:
            character.y_velocity += RUN_SPEED_PPS



    @staticmethod
    def exit(character, event):
        if event == SPACE:
            character.fire_ball()

    @staticmethod
    def do(character):
        character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        character.x += character.x_velocity * game_framework.frame_time
        character.y += character.y_velocity * game_framework.frame_time

        character.x = clamp(character.canvas_width // 2, character.x, character.bg.w - character.canvas_width // 2)
        character.y = clamp(character.canvas_height // 2, character.y, character.bg.h - character.canvas_height // 2)


    @staticmethod
    def draw(character):
        cx, cy = character.canvas_width//2, character.canvas_height//2

        if character.x_velocity > 0:
            character.image.clip_draw(int(character.frame) * 100, 0, 100, 100, cx, cy)
            character.dir = 1
        elif character.x_velocity < 0:
            character.image.clip_draw(int(character.frame) * 100, 0, 100, 100, cx, cy)
            character.dir = -1
        else:
            # if character x_velocity == 0
            if character.y_velocity > 0 or character.y_velocity < 0:
                if character.dir == 1:
                    character.image.clip_draw(int(character.frame) * 100, 100, 100, 100, cx, cy)
                else:
                    character.image.clip_draw(int(character.frame) * 100, 0, 100, 100, cx, cy)
            else:
                # character is idle
                if character.dir == 1:
                    character.image.clip_draw(int(character.frame) * 100, 300, 100, 100, cx, cy)
                else:
                    character.image.clip_draw(int(character.frame) * 100, 200, 100, 100, cx, cy)


next_state_table = {
    WalkingState: {
                UPKEY_UP: WalkingState, UPKEY_DOWN: WalkingState, DOWNKEY_UP: WalkingState, DOWNKEY_DOWN: WalkingState,
                SPACE: WalkingState}
}


class Character:

    def __init__(self):
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        # Character is only once created, so instance image loading is fine
        self.image = load_image('BraveCookie.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.x_velocity, self.y_velocity = (RUN_SPEED_MPS * PIXEL_PER_METER), 0
        self.frame = 0
        self.event_que = []
        self.cur_state = WalkingState
        self.cur_state.enter(self, None)

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50


    def set_background(self, bg):
        self.bg = bg
        self.x = 0
        self.y = self.bg.h / 2

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
            self.x_velocity += RUN_SPEED_PPS

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.canvas_width//2 - 60, self.canvas_height//2 + 50, '(%5d, %5d)' % (self.x, self.y), (255, 255, 0))

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
