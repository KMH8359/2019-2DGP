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
FRAMES_PER_ACTION = 4
JUMPCOUNT = 0
DOUBLEJUMPCOUNT = 0
DEATHCOUNT = 0
JUMPING = 0

# Character Event
UPKEY_DOWN, DOWNKEY_DOWN,UPKEY_UP, DOWNKEY_UP, SPACE, STOP_JUMP,LSHIFT, COOKIE1, COOKIE2, COOKIE3, COOKIE4, COOKIE5 = range(12)

key_event_table = {
    (SDL_KEYDOWN, SDLK_UP): UPKEY_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWNKEY_DOWN,
    (SDL_KEYUP, SDLK_UP): UPKEY_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWNKEY_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_LSHIFT): LSHIFT,
    (SDL_KEYDOWN, SDLK_1): COOKIE1,
    (SDL_KEYDOWN, SDLK_2): COOKIE2,
    (SDL_KEYDOWN, SDLK_3): COOKIE3,
    (SDL_KEYDOWN, SDLK_4): COOKIE4,
    (SDL_KEYDOWN, SDLK_5): COOKIE5  
}


# Character States

class WalkingState:
    frameY = 272
    frameX = 272
    @staticmethod
    def enter(character, event):
        pass
        #if event == UPKEY_DOWN:
            #character.cur_state = JumpingState
            #character.cur_state.enter(character, None)
        #if event == UPKEY_UP:
         #   character.y_velocity -= RUN_SPEED_PPS
        #if event == DOWNKEY_DOWN:
         #   character.y_velocity -= RUN_SPEED_PPS
        #elif event == DOWNKEY_UP:
         #   character.y_velocity += RUN_SPEED_PPS



    @staticmethod
    def do(character):
        global FRAMES_PER_ACTION
        FRAMES_PER_ACTION = 4
        character.runspeed = 4
        character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        character.x += character.runspeed  * character.x_velocity * game_framework.frame_time
        character.y += character.y_velocity * game_framework.frame_time

    @staticmethod
    def draw(character):
        global frameX,frameY
        cx, cy = character.canvas_width//8, 240

        if character.x_velocity > 0:
            character.image.clip_draw(int(character.frame) * 270 + 10 , 1090, 240, 240, character.cx, character.cy,character.sizeX,character.sizeY)
            character.dir = 1
        else:
            # if character x_velocity == 0
            if character.y_velocity > 0 or character.y_velocity < 0:
                if character.dir == 1:
                    character.image.clip_draw(int(character.frame) * 270 + 10 , 1090, 260, 270, cx, cy)
class RunningState:
    frameY = 272
    frameX = 272
    @staticmethod
    def enter(character, event):
        pass
        #if event == UPKEY_DOWN:
            #character.cur_state = JumpingState
            #character.cur_state.enter(character, None)
        #if event == UPKEY_UP:
         #   character.y_velocity -= RUN_SPEED_PPS
        #if event == DOWNKEY_DOWN:
         #   character.y_velocity -= RUN_SPEED_PPS
        #elif event == DOWNKEY_UP:
         #   character.y_velocity += RUN_SPEED_PPS



    @staticmethod
    def exit(character, event):
        if event == SPACE:
            character.fire_ball()

    @staticmethod
    def do(character):
        global FRAMES_PER_ACTION
        FRAMES_PER_ACTION = 4
        character.runspeed = 8
        character.invincible = 10000000
        character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        character.x += character.runspeed * character.x_velocity * game_framework.frame_time
        character.y += character.y_velocity * game_framework.frame_time


    @staticmethod
    def draw(character):
        global frameX,frameY
        cx, cy = character.canvas_width//8, 240

        if character.x_velocity > 0:
            character.image.clip_draw(int(character.frame + 4) * 270 + 20 , 1090, 240, 240, character.cx, character.cy,character.sizeX,character.sizeY)
            character.dir = 1
        else:
            # if character x_velocity == 0
            if character.y_velocity > 0 or character.y_velocity < 0:
                if character.dir == 1:
                    character.image.clip_draw(int(character.frame) * 270 + 10 , 1090, 260, 270, cx, cy)
class JumpingState:
    frameY = 0
    frameX = 272
    @staticmethod
    def enter(character, event):
        pass
        #if event == UPKEY_DOWN:
         #   character.y_velocity += RUN_SPEED_PPS
        #elif event == UPKEY_UP:
         #   character.y_velocity -= RUN_SPEED_PPS
        #if event == DOWNKEY_DOWN:
         #   character.y_velocity -= RUN_SPEED_PPS
        #elif event == DOWNKEY_UP:
         #   character.y_velocity += RUN_SPEED_PPS


    @staticmethod
    def exit(character, event):
        if event == SPACE:
            character.fire_ball()

    @staticmethod
    def do(character):
        global FRAMES_PER_ACTION
        global JUMPCOUNT
        global JUMPING
        if JUMPCOUNT >= 0 and JUMPCOUNT < 100:
            JUMPING += 3
        elif JUMPCOUNT >= 100 and JUMPCOUNT < 200:
            JUMPING -= 3
        if JUMPCOUNT % 200 == 0:
            JUMPING = 0
            JUMPCOUNT = 0
            character.add_event(STOP_JUMP)
            
        JUMPCOUNT += 1
        FRAMES_PER_ACTION = 2
        #character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        character.frame = 7
        if JUMPCOUNT > 180:
            character.frame = 6
        character.x += character.runspeed * character.x_velocity * game_framework.frame_time
        character.y += character.y_velocity * game_framework.frame_time




    @staticmethod
    def draw(character):
        global frameX,frameY
        global JUMPING
        cx, cy = character.canvas_width//8, 240

        if character.x_velocity > 0:
            character.image.clip_draw(int(character.frame) * 270 + 20 , 1365, 240, 240, character.cx, character.cy + JUMPING,character.sizeX,character.sizeY)
            character.dir = 1
        elif character.x_velocity < 0:
            character.image.clip_draw(int(character.frame) * 272, 0, 300, 270, cx, cy)
            character.dir = -1
        else:
            # if character x_velocity == 0
            if character.y_velocity > 0 or character.y_velocity < 0:
                if character.dir == 1:
                    character.image.clip_draw(int(character.frame) * 270 + 10 , 0, 260, 270, cx, cy)
                else:
                    character.image.clip_draw(int(character.frame) * 270, 1040, 300, 300, cx, cy)
            else:
                # character is idle
                if character.dir == 1:
                    character.image.clip_draw(int(character.frame) * 270 + 10 , 0, 260, 270, cx, cy)
                else:
                    character.image.clip_draw(int(character.frame) * 300, 1040, 300, 300, cx, cy)
                    
class DoubleJumpingState:
    frameY = 0
    frameX = 272
    @staticmethod
    def enter(character, event):
        pass
        #if event == UPKEY_DOWN:
         #   character.y_velocity += RUN_SPEED_PPS
        #elif event == UPKEY_UP:
         #   character.y_velocity -= RUN_SPEED_PPS
        #if event == DOWNKEY_DOWN:
         #   character.y_velocity -= RUN_SPEED_PPS
        #elif event == DOWNKEY_UP:
         #   character.y_velocity += RUN_SPEED_PPS


    @staticmethod
    def exit(character, event):
        if event == SPACE:
            character.fire_ball()

    @staticmethod
    def do(character):
        global FRAMES_PER_ACTION
        global JUMPING
        global JUMPCOUNT
        global DOUBLEJUMPCOUNT
            
        if DOUBLEJUMPCOUNT >= 0 and DOUBLEJUMPCOUNT < 100:
            JUMPING += 3
        elif DOUBLEJUMPCOUNT >= 100:
            JUMPING -= 3
        if JUMPING == 0:
            JUMPCOUNT = 0
            DOUBLEJUMPCOUNT = 0
            character.add_event(STOP_JUMP)
            
        DOUBLEJUMPCOUNT += 1
        FRAMES_PER_ACTION = 6
        #character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        if DOUBLEJUMPCOUNT < 30:
            character.frame = 1
        elif 30 <= DOUBLEJUMPCOUNT and DOUBLEJUMPCOUNT < 60:
            character.frame = 1
        elif 60 <= DOUBLEJUMPCOUNT and DOUBLEJUMPCOUNT < 90:
            character.frame = 2
        elif 90 <= DOUBLEJUMPCOUNT and DOUBLEJUMPCOUNT < 120:
            character.frame = 3
        elif 120 <= DOUBLEJUMPCOUNT and DOUBLEJUMPCOUNT < 150:
            character.frame = 4
        elif 150 <= DOUBLEJUMPCOUNT:
            character.frame = 5
        character.x += character.runspeed * character.x_velocity * game_framework.frame_time
        character.y += character.y_velocity * game_framework.frame_time



    @staticmethod
    def draw(character):
        global frameX,frameY
        cx, cy = character.canvas_width//8, 240

        if character.x_velocity > 0:
            character.image.clip_draw(int(character.frame) * 270 + 15 , 1365, 240, 240, character.cx, character.cy + JUMPING,character.sizeX,character.sizeY)
            character.dir = 1
        elif character.x_velocity < 0:
            character.image.clip_draw(int(character.frame) * 272, 0, 300, 270, cx, cy)
            character.dir = -1
        else:
            # if character x_velocity == 0
            if character.y_velocity > 0 or character.y_velocity < 0:
                if character.dir == 1:
                    character.image.clip_draw(int(character.frame) * 270 + 10 , 0, 260, 270, cx, cy)
                else:
                    character.image.clip_draw(int(character.frame) * 270, 1040, 300, 300, cx, cy)
            else:
                # character is idle
                if character.dir == 1:
                    character.image.clip_draw(int(character.frame) * 270 + 10 , 0, 260, 270, cx, cy)
                else:
                    character.image.clip_draw(int(character.frame) * 300, 1040, 300, 300, cx, cy)
class SlidingState:
    frameY = 0
    frameX = 272
    @staticmethod
    def enter(character, event):
        pass

    @staticmethod
    def exit(character, event):
        if event == SPACE:
            character.fire_ball()

    @staticmethod
    def do(character):
        global FRAMES_PER_ACTION
        FRAMES_PER_ACTION = 2
        character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        character.x += character.runspeed * character.x_velocity * game_framework.frame_time
        character.y += character.y_velocity * game_framework.frame_time




    @staticmethod
    def draw(character):
        global frameX,frameY
        cx, cy = character.canvas_width//8, 240

        if character.x_velocity > 0:
            character.image.clip_draw(int(character.frame) * 270 + 2460 , 1365, 240, 240, character.cx, character.cy,character.sizeX,character.sizeY)
            character.dir = 1
        elif character.x_velocity < 0:
            character.image.clip_draw(int(character.frame) * 272, 0, 300, 270, cx, cy)
            character.dir = -1
        else:
            # if character x_velocity == 0
            if character.y_velocity > 0 or character.y_velocity < 0:
                if character.dir == 1:
                    character.image.clip_draw(int(character.frame) * 270 + 10 , 0, 260, 270, cx, cy)
                else:
                    character.image.clip_draw(int(character.frame) * 270, 1040, 300, 300, cx, cy)
            else:
                # character is idle
                if character.dir == 1:
                    character.image.clip_draw(int(character.frame) * 270 + 10 , 0, 260, 270, cx, cy)
                else:
                    character.image.clip_draw(int(character.frame) * 300, 1040, 300, 300, cx, cy)
class Dead:
    @staticmethod
    def enter(character, event):
        pass

    @staticmethod
    def exit(character, event):
        if event == SPACE:
            character.fire_ball()

    @staticmethod
    def do(character):
        global FRAMES_PER_ACTION
        FRAMES_PER_ACTION = 2
        global DEATHCOUNT
        
        DEATHCOUNT += 1
        FRAMES_PER_ACTION = 5
        #character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        if DEATHCOUNT < 30:
            character.frame = 0
        elif 30 <= DEATHCOUNT and DEATHCOUNT < 60:
            character.frame = 1
        elif 60 <= DEATHCOUNT and DEATHCOUNT < 90:
            character.frame = 2
        elif 90 <= DEATHCOUNT and DEATHCOUNT < 120:
            character.frame = 3
        elif 120 <= DEATHCOUNT:
            character.frame = 4



    @staticmethod
    def draw(character):
        character.image.clip_draw(int(character.frame) * 270 + 1370 , 270, 240, 240, character.cx, character.cy,character.sizeX,character.sizeY)



next_state_table = {
    WalkingState: {
                UPKEY_UP: JumpingState, UPKEY_DOWN: JumpingState, DOWNKEY_UP: SlidingState, DOWNKEY_DOWN: SlidingState,
                SPACE: RunningState, LSHIFT: WalkingState,COOKIE1:Dead},
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
    Dead: {
                UPKEY_UP: Dead, UPKEY_DOWN: Dead, DOWNKEY_UP: Dead,
                DOWNKEY_DOWN: Dead, SPACE: Dead, STOP_JUMP: Dead}
    
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
        self.HP = 100
        self.runspeed = 4
        self.cx, self.cy = self.canvas_width // 8, 240
        self.frame = 0
        self.invincible = 0 # 무적시간
        self.bigger = False # 커져라 아이템 사용중 여부
        self.event_que = []
        self.cur_state = WalkingState
        self.sizeX, self.sizeY = 240, 240
        self.cur_state.enter(self, None)

    def get_bb(self):
        if self.cur_state == SlidingState:
            return self.cx - 80,self.cy - 120,self.cx + 80,self.cy - 70
        elif self.bigger == True:
            return self.cx - 200, self.cy - 400,self.cx + 200,self.cy + 100
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
        if self.invincible > 0:
            self.invincible -= 1
        if self.HP <= 0:
            self.cur_state = Dead
            self.cur_state.enter(self, None)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)


    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())
        #self.font.draw(self.canvas_width//2 - 60, self.canvas_height//2 + 50, '(%5d, %5d)' % (self.x, self.y), (255, 255, 0))

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            if key_event == LSHIFT:
                if self.cy < 300:
                    self.sizeX,self.sizeY = 800, 800
                    self.cy = 520
                    self.invincible = 10000
                    self.bigger = True
                else:
                    self.sizeX,self.sizeY = 240, 240
                    self.cy = 240
                    self.invincible = 0
                    self.bigger = False
            if key_event == COOKIE2:
                self.HP -= 100
            self.add_event(key_event)

