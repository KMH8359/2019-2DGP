import game_framework
from pico2d import *
import main_state
import gameLobby

name = "ShopState"
image = None
shopType = None
font = None

with open('saveData.json', 'r') as f:
    data_list = json.load(f)

HPUpgradeLevel = data_list['HPLevel']
JellyUpgradeLevel = data_list['JellyLevel']
HPUpgradeCost = HPUpgradeLevel * 1000
JellyUpgradeCost = JellyUpgradeLevel * 1000
HPValue = HPUpgradeLevel * 50
JellyValue = JellyUpgradeLevel * 100
game_start_sound = None


def enter():
    global image
    global font
    global shopType
    global game_start_sound

    image = load_image('shopHP.png')
    font = load_font('CookieRunFont.ttf', 27)
    shopType = 'HPshop'
    game_start_sound = load_wav('game_start_sound.wav')
    game_start_sound.set_volume(64)


def exit():
    global image
    del image


mouseX, mouseY = 0, 0


def handle_events():
    global mouseX, mouseY
    global shopType
    global image
    global HPUpgradeLevel
    global JellyUpgradeLevel
    global HPUpgradeCost
    global JellyUpgradeCost
    global HPValue
    global JellyValue
    global data_list

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
            if 700 <= mouseX <= 1000 and 0 <= mouseY < 150:  # 게임시작
                game_start_sound.play()
                delay(0.5)
                game_framework.change_state(main_state)
            elif 560 <= mouseX <= 610 and 660 <= mouseY < 720:
                delay(0.2)
                game_framework.change_state(gameLobby)
            elif 330 <= mouseX <= 450 and 480 <= mouseY <= 630 and shopType == 'HPshop':  # 젤리 점수 ++
                shopType = 'Jellyshop'
                image = load_image('shopJelly.png')
            elif 210 <= mouseX <= 320 and 480 <= mouseY <= 630:  # 캐릭터 HP ++
                shopType = 'HPshop'
                image = load_image('shopHP.png')
            elif 780 <= mouseX <= 970 and 440 <= mouseY <= 510:  # 업그레이드
                if shopType == 'HPshop' and gameLobby.point >= HPUpgradeLevel * 1000:
                    gameLobby.point -= HPUpgradeLevel * 1000
                    data_list['Point'] -= HPUpgradeLevel * 1000
                    data_list['HPLevel'] += 1
                    HPUpgradeLevel += 1
                    HPUpgradeCost = HPUpgradeLevel * 1000
                    HPValue += 50
                elif shopType == 'Jellyshop' and gameLobby.point >= JellyUpgradeLevel * 1000:
                    gameLobby.point -= JellyUpgradeLevel * 1000
                    data_list['Point'] -= JellyUpgradeLevel * 1000
                    data_list['JellyLevel'] += 1
                    JellyUpgradeLevel += 1
                    JellyUpgradeCost = JellyUpgradeLevel * 1000
                    JellyValue += 100
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()

        with open('saveData.json', 'w', encoding='utf-8') as make_file:
            json.dump(data_list, make_file, indent="\t")



def draw():
    global shopType
    image.draw(600, 400, 1200, 800)
    font.draw(520, 760, ' %5d ' % gameLobby.point, (255, 0, 0))
    font.draw(220, 500, ' Lv%02d' % HPUpgradeLevel, (255, 0, 255))
    font.draw(340, 500, ' Lv%02d' % JellyUpgradeLevel, (255, 0, 255))
    if shopType == 'HPshop':
        font.draw(860, 550, ' %5d' % HPUpgradeCost, (0, 0, 255))
        font.draw(800, 600, '체력 강화 Lv%02d' % HPUpgradeLevel, (0, 0, 255))
        font.draw(810, 350, '%2d' % HPValue, (0, 0, 255))
    else:
        font.draw(860, 550, ' %5d' % JellyUpgradeCost, (0, 0, 255))
        font.draw(800, 600, '젤리 강화 Lv%02d' % JellyUpgradeLevel, (0, 0, 255))
        font.draw(650, 325, '젤리 획득 점수 %2d 증가' % JellyValue, (0, 0, 255))


def update():
    pass


def pause():
    pass


def resume():
    pass
