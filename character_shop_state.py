import game_framework
from pico2d import *
import main_state
import gameLobby

name = "CharacterShopState"
image = None
ChoosedImage = None
CostImage = None
NotChoosedImage = None
font = None
BraveCookieSelected = True
BrightCookieSelected = False
BrightCookieHave = False
ButterCreamCookieSelected = False
ButterCreamCookieHave = False
CloudCookieSelected = False
CloudCookieHave = False



def enter():
    global image
    global font
    global ChoosedImage
    global CostImage
    global NotChoosedImage

    image = load_image('shopCharacter.png')
    ChoosedImage = load_image('characterChoosed.png')
    CostImage = load_image('characterCost.png')
    NotChoosedImage = load_image('characterNotChoosed.png')
    font = load_font('CookieRunFont.ttf', 27)


def exit():
    global image
    del image


mouseX, mouseY = 0, 0


def handle_events():
    global mouseX, mouseY
    global image
    global BraveCookieSelected
    global BrightCookieSelected
    global CloudCookieSelected
    global ButterCreamCookieSelected

    global BrightCookieHave
    global CloudCookieHave
    global ButterCreamCookieHave

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            mouseX, mouseY = event.x, 800 - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.type == SDLK_0:
            gameLobby.point += 10000
        elif event.type == SDL_MOUSEBUTTONDOWN:
            gameLobby.click_sound.play()
            if 1040 <= mouseX <= 1080 and 635 <= mouseY <= 685:
                delay(0.2)
                game_framework.change_state(gameLobby)
            elif 140 <= mouseX <= 330 and 50 <= mouseY <= 130 and BraveCookieSelected == False:  # 용감한 쿠키
                BraveCookieSelected = True
                BrightCookieSelected = False
                CloudCookieSelected = False
                ButterCreamCookieSelected = False
            elif 390 <= mouseX <= 580 and 50 <= mouseY < 130:  # 명랑한 쿠키
                if BrightCookieHave == False and gameLobby.point >= 10000:
                    gameLobby.point -= 10000
                    BrightCookieSelected = True
                    BrightCookieHave = True
                    BraveCookieSelected = False
                    CloudCookieSelected = False
                    ButterCreamCookieSelected = False
                elif BrightCookieSelected == False and BrightCookieHave:
                    BraveCookieSelected = False
                    BrightCookieSelected = True
                    CloudCookieSelected = False
                    ButterCreamCookieSelected = False
            elif 640 <= mouseX <= 830 and 50 <= mouseY < 130:  # 구름맛 쿠키
                if CloudCookieHave == False and gameLobby.point >= 15000:
                    gameLobby.point -= 15000
                    CloudCookieSelected = True
                    CloudCookieHave = True
                    BraveCookieSelected = False
                    BrightCookieSelected = False
                    ButterCreamCookieSelected = False
                elif CloudCookieSelected == False and CloudCookieHave:
                    BraveCookieSelected = False
                    BrightCookieSelected = False
                    CloudCookieSelected = True
                    ButterCreamCookieSelected = False
            elif 880 <= mouseX <= 1070 and 50 <= mouseY <= 130:  # 버터크림맛 쿠키
                if ButterCreamCookieHave == False and gameLobby.point >= 20000:
                    gameLobby.point -= 20000
                    ButterCreamCookieSelected = True
                    ButterCreamCookieHave = True
                    BraveCookieSelected = False
                    CloudCookieSelected = False
                    BrightCookieSelected = False
                elif ButterCreamCookieSelected == False and ButterCreamCookieHave:
                    BraveCookieSelected = False
                    BrightCookieSelected = False
                    CloudCookieSelected = False
                    ButterCreamCookieSelected = True



        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()


def draw():
    image.draw(600, 400, 1200, 800)
    if BraveCookieSelected:
        ChoosedImage.draw(235, 90, 190, 80)
    else:
        NotChoosedImage.draw(235, 90, 190, 80)

    if BrightCookieSelected:
        ChoosedImage.draw(485, 90, 190, 80)
    elif BrightCookieHave and BrightCookieSelected == False:
        NotChoosedImage.draw(485, 90, 190, 80)
    elif not BrightCookieHave:
        CostImage.draw(485, 90, 190, 80)
        font.draw(470, 90, '10000', (255, 0, 255))

    if CloudCookieSelected:
        ChoosedImage.draw(735, 90, 190, 80)
    elif CloudCookieHave and CloudCookieSelected == False:
        NotChoosedImage.draw(735, 90, 190, 80)
    elif not CloudCookieHave:
        CostImage.draw(735, 90, 190, 80)
        font.draw(720, 90, '15000', (255, 0, 255))

    if ButterCreamCookieSelected:
        ChoosedImage.draw(975, 90, 190, 80)
    elif ButterCreamCookieHave and ButterCreamCookieSelected == False:
        NotChoosedImage.draw(975, 90, 190, 80)
    elif not ButterCreamCookieHave:
        CostImage.draw(975, 90, 190, 80)
        font.draw(960, 90, '20000', (255, 0, 255))

    font.draw(520, 760, ' %5d ' % gameLobby.point, (255, 0, 0))


def update():
    pass


def pause():
    pass


def resume():
    pass
