import game_framework
from pico2d import *
import main_state
import game_world

# Character Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4
JUMPCOUNT = 0
DOUBLEJUMPCOUNT = 0
DEATHCOUNT = 0
JUMPING = 0
JUMPPOWER = 0

# Character Event
UPKEY_DOWN, DOWNKEY_DOWN, UPKEY_UP, DOWNKEY_UP, SPACE, STOP_JUMP, LSHIFT = range(7)

key_event_table = {
    (SDL_KEYDOWN, SDLK_UP): UPKEY_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWNKEY_DOWN,
    (SDL_KEYUP, SDLK_UP): UPKEY_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWNKEY_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_LSHIFT): LSHIFT,
}


# Character States

class WalkingState:
    @staticmethod
    def enter(character, event):
        global FRAMES_PER_ACTION
        FRAMES_PER_ACTION = 4

    @staticmethod
    def do(character):
        character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME
                           * game_framework.frame_time) % FRAMES_PER_ACTION

    @staticmethod
    def draw(character):
        if character.running:
            character.image.clip_draw(int(character.frame + 4) * 270 + 20, 1090, 240, 240, character.cx, character.cy,
                                      character.sizeX, character.sizeY)
        else:
            character.image.clip_draw(int(character.frame) * 270 + 10, 1090, 240, 240, character.cx, character.cy,
                                      character.sizeX, character.sizeY)


class RunningState:
    @staticmethod
    def enter(character, event):
        global FRAMES_PER_ACTION
        FRAMES_PER_ACTION = 4

    @staticmethod
    def do(character):
        character.cx, character.cy = character.canvas_width // 8, 240
        character.invincible = 10000000
        character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME *game_framework.frame_time) % FRAMES_PER_ACTION

    @staticmethod
    def draw(character):
        character.image.clip_draw(int(character.frame + 4) * 270 + 20, 1090, 240, 240, character.cx, character.cy,
                                  character.sizeX, character.sizeY)


class JumpingState:
    @staticmethod
    def enter(character, event):
        # global FRAMES_PER_ACTION
        # FRAMES_PER_ACTION = 2
        global JUMPPOWER
        JUMPPOWER = 100
        pass

    @staticmethod
    def do(character):
        global JUMPCOUNT
        global JUMPING
        global JUMPPOWER

        JUMPING += JUMPPOWER * FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time

        if JUMPING < 0:
            JUMPING = 0
            character.add_event(STOP_JUMP)

        JUMPPOWER -= FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time * 25
        # character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        character.frame = 7

    @staticmethod
    def draw(character):
        global JUMPING
        character.image.clip_draw(int(character.frame) * 270 + 20, 1365, 240, 240, character.cx, character.cy + JUMPING,
                                  character.sizeX, character.sizeY)


class DoubleJumpingState:
    @staticmethod
    def enter(character, event):
        global JUMPPOWER
        # global FRAMES_PER_ACTION
        # FRAMES_PER_ACTION = 6
        JUMPPOWER = 100
        pass

    @staticmethod
    def do(character):
        global JUMPING
        global DOUBLEJUMPCOUNT
        global JUMPPOWER

        JUMPING += JUMPPOWER * FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time

        if JUMPING <= 0:
            JUMPING = 0
            DOUBLEJUMPCOUNT = 0
            character.add_event(STOP_JUMP)

        JUMPPOWER -= FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time * 25
        DOUBLEJUMPCOUNT += FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time * 25
        # character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION

        if 0 <= DOUBLEJUMPCOUNT < 30:
            character.frame = 1
        elif 30 <= DOUBLEJUMPCOUNT < 60:
            character.frame = 2
        elif 60 <= DOUBLEJUMPCOUNT < 90:
            character.frame = 3
        elif 90 <= DOUBLEJUMPCOUNT < 120:
            character.frame = 4
        elif 120 <= DOUBLEJUMPCOUNT:
            character.frame = 5

    @staticmethod
    def draw(character):
        character.image.clip_draw(int(character.frame) * 270 + 15, 1365, 240, 240, character.cx, character.cy + JUMPING,
                                  character.sizeX, character.sizeY)


class SlidingState:
    @staticmethod
    def enter(character, event):
        global FRAMES_PER_ACTION
        FRAMES_PER_ACTION = 2

    @staticmethod
    def do(character):
        character.frame = (
                                  character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION

    @staticmethod
    def draw(character):
        character.image.clip_draw(int(character.frame) * 270 + 2460, 1365, 240, 240, character.cx, character.cy,
                                  character.sizeX, character.sizeY)


class DeathState:
    @staticmethod
    def enter(character, event):
        global FRAMES_PER_ACTION
        FRAMES_PER_ACTION = 2

    @staticmethod
    def do(character):
        global DEATHCOUNT

        DEATHCOUNT += game_framework.frame_time
        # character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        if DEATHCOUNT < 30:
            character.frame = 0
        elif 30 <= DEATHCOUNT < 60:
            character.frame = 1
        elif 60 <= DEATHCOUNT < 90:
            character.frame = 2
        elif 90 <= DEATHCOUNT < 120:
            character.frame = 3
        elif 120 <= DEATHCOUNT:
            character.frame = 4

    @staticmethod
    def draw(character):
        character.image.clip_draw(int(character.frame) * 270 + 1370, 270, 240, 240, character.cx, character.cy,
                                  character.sizeX, character.sizeY)


next_state_table = {
    WalkingState: {
        UPKEY_UP: JumpingState, UPKEY_DOWN: JumpingState, DOWNKEY_UP: SlidingState, DOWNKEY_DOWN: SlidingState,
        SPACE: RunningState, LSHIFT: WalkingState},
    RunningState: {
        UPKEY_UP: JumpingState, UPKEY_DOWN: JumpingState, DOWNKEY_UP: WalkingState, DOWNKEY_DOWN: SlidingState,
        SPACE: WalkingState},
    JumpingState: {
        UPKEY_UP: JumpingState, UPKEY_DOWN: DoubleJumpingState, DOWNKEY_UP: JumpingState, DOWNKEY_DOWN: JumpingState,
        SPACE: JumpingState, STOP_JUMP: WalkingState},
    SlidingState: {
        UPKEY_UP: JumpingState, UPKEY_DOWN: JumpingState, DOWNKEY_UP: WalkingState, DOWNKEY_DOWN: WalkingState,
        SPACE: JumpingState},
    DoubleJumpingState: {
        UPKEY_UP: DoubleJumpingState, UPKEY_DOWN: DoubleJumpingState, DOWNKEY_UP: DoubleJumpingState,
        DOWNKEY_DOWN: DoubleJumpingState, SPACE: DoubleJumpingState, STOP_JUMP: WalkingState},
    DeathState: {
        UPKEY_UP: DeathState, UPKEY_DOWN: DeathState, DOWNKEY_UP: DeathState,
        DOWNKEY_DOWN: DeathState, SPACE: DeathState, STOP_JUMP: DeathState}

}


class Character:

    def __init__(self):
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        # Character is only once created, so instance image loading is fine
        self.image = load_image('BraveCookie.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.score = 0
        self.HP = 500
        self.cx, self.cy = self.canvas_width // 8, 240
        self.frame = 0
        self.invincible = 0  # 무적시간
        self.bigger = False  # 커져라 아이템 사용중 여부
        self.running = False # 부스터 아이템 사용중 여부
        self.event_que = []
        self.cur_state = WalkingState
        self.sizeX, self.sizeY = 240, 240
        self.cur_state.enter(self, None)

    def get_bb(self):
        if self.cur_state == SlidingState:
            if self.bigger:
                return self.cx - 300, self.cy - 400, self.cx + 300, self.cy - 100
            else:
                return self.cx - 80, self.cy - 120, self.cx + 80, self.cy - 70
        elif self.bigger:
            return self.cx - 200, self.cy - 400, self.cx + 200, self.cy + 100
        else:
            return self.cx - 50, self.cy - 100 + JUMPING, self.cx + 70, self.cy + 20 + JUMPING

    def set_background(self, bg):
        self.bg = bg
        self.x = 0
        self.y = self.bg.h / 2

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        self.HP -= game_framework.frame_time * main_state.scrollspeed / 100
        if self.invincible > 0:
            self.invincible -= 1
        if self.bigger:
            self.sizeX, self.sizeY = 800, 800
            self.cy = 520
            self.invincible = 1000
        if self.running:
            self.invincible = 1000
        if self.HP <= 0:
            self.cur_state = DeathState
            self.cur_state.enter(self, None)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(1000, 700, 'Score: %5d' % self.score, (255, 255, 0))
        draw_rectangle(*self.get_bb())
        # self.font.draw(self.canvas_width//2 - 60, self.canvas_height//2 + 50, '(%5d, %5d)' % (self.x, self.y), (255, 255, 0))

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)



