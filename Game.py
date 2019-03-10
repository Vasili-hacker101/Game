import sys
import pygame
from PIL import Image
from Player import *
from Blocks import Platform
from Items import *
from Levels import *
from Monsters import *

WIN_WIDTH = 1280
WIN_HEIGHT = 720
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "black"
BACKGROUND_IMAGE_MENU = pygame.image.load("./images/Background/Background.png")


class Menu:

    def __init__(self, punkts):
        self.punkts = punkts
        self.background = BACKGROUND_IMAGE_MENU

    def render(self, canvas, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                canvas.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                canvas.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def menu(self, last_frame=False):
        global screen
        done = True
        font_menu = pygame.font.SysFont("Comic Sans MS", 100, True)
        font_name = pygame.font.SysFont("Comic Sans MS", 120, True)
        name_of_game = pygame.Surface((1280, 180))
        name_of_game_str = u"  while True"
        name_of_game.fill((0, 0, 0))
        name_of_game.set_colorkey((0, 0, 0))
        name_of_game.blit(font_name.render(name_of_game_str, 1, (255, 255, 255)), (10, 5))
        pygame.key.set_repeat(0,0)
        pygame.mouse.set_visible(True)
        punkt = 0
        if last_frame:
            pygame.image.save(pygame.display.get_surface(), "./images/Background/last_frame.jpeg")
            pil_image = Image.open("./images/Background/last_frame.jpeg")
            x, y = pil_image.width, pil_image.height
            pixels = pil_image.load()
            im2 = Image.new('RGB', (1280, 720), (0, 0, 0))
            pixels2 = im2.load()
            for i in range(x):
                for j in range(y):
                    r, g, b = pixels[i, j]
                    bw = (r + g + b) // 3
                    pixels2[i, j] = bw, bw, bw
            im2.save("./images/Background/last_frame.jpeg")
            self.background = pygame.image.load("./images/Background/last_frame.jpeg")

        while done:
            screen.fill((0, 0, 0))
            screen.blit(self.background, (0, 0))
            screen.blit(name_of_game, (0, 50))
            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0] > i[0] and mp[0] < i[0] + 180 and mp[1] > i[1] and mp[1] < i[1] + 100:
                    punkt = i[5]
            self.render(screen, font_menu, punkt)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()

                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()

                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts)-1:
                            punkt += 1
                    if e.key == pygame.K_RETURN or\
                       e.key == pygame.K_KP_ENTER:
                            if punkt == 0:
                                done = False
                            elif punkt == 1:
                                sys.exit()

                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                         done = False
                    elif punkt == 1:
                         sys.exit()

            pygame.display.flip()


# О П И С А Н И Е  К А М Е Р Ы


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def camera_configure(cam, target_rect):
    l = -target_rect.x + WIN_WIDTH / 2
    t = -target_rect.y + WIN_HEIGHT / 2

    w, h = cam.width, cam.height

    l = min(0, l)
    l = max(-(cam.width - WIN_WIDTH), l)
    t = max(-(cam.height - WIN_HEIGHT), t)
    t = min(0, t)

    return Rect(l, t, w, h)

# Ф У Н К Ц И Я  О Т Р И С О В К И  К А Д Р А


def Draw_Game(do_flip):
    global screen
    screen.blit(bg, (0, 0))

    for i in items:
        i.update(hero)

    for i in platforms:
        if isinstance(i, Flame) or\
           isinstance(i, Right_Arrow) or\
           isinstance(i, Left_Arrow):
            i.update()
        elif isinstance(i, Exit):
            i.update(hero)

    for i in monsters:
        i.update(platforms)

    camera.update(hero)
    hero.update(run, left, right, up, platforms + items, monsters)


    for e in entities:
        screen.blit(e.image, camera.apply(e))

    info.fill((0, 0, 0))
    info_str = u"Счет: " + str(hero.num_of_coins)
    info_str += f"   Уровень: {num_of_level + 1}"
    info_str += f"   Жизни: {hero.hp}"
    if hero.num_of_keycards > 0:
        info_str += ", Ключ!"

    info.blit(info_font.render(info_str, 1, (255, 255, 255)), (10, 5))

    message.fill((0, 0, 0))
    message.set_colorkey((0, 0, 0))
    if hero.level_passed:

        lvl_passed_str = u"            Вы прошли уровень " + str(num_of_level + 1)
        if num_of_level == len(levels) - 1:
            lvl_passed_str = u"       Вы прошли игру! Ваш счет: " + str(hero.num_of_coins)
        message.blit(message_font.render(lvl_passed_str, 1, (255, 255, 255)), (10, 5))

    if do_flip:
        flip_it = pygame.transform.flip(pygame.display.get_surface(), 0, 1)
        screen.blit(flip_it, (0, 0))
    else:
        screen.blit(e.image, (0, 0))
    screen.blit(info, (0, 0))
    screen.blit(message, (0, 300))
    pygame.display.update()


def create_level(level):
    global entities, platforms, items, monsters
    entities = pygame.sprite.Group()
    platforms = []
    items = []
    monsters = []
    x = y = 0
    num = 1
    for row in level:
        for col in row:
            if col == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)

            elif col == "*":
                flame = Flame(x, y)
                entities.add(flame)
                platforms.append(flame)

            elif col == ">":
                rarrow = Right_Arrow(x, y)
                entities.add(rarrow)
                platforms.append(rarrow)

            elif col == "<":
                larrow = Left_Arrow(x, y)
                entities.add(larrow)
                platforms.append(larrow)

            elif col == "^":
                trampoline = Trampoline(x, y)
                entities.add(trampoline)
                platforms.append(trampoline)

            elif col == "e":
                exit = Exit(x, y)
                entities.add(exit)
                platforms.append(exit)

            elif col == "m":
                monster = FireBall(x, y)
                entities.add(monster)
                monsters.append(monster)

            elif col == "+":
                item = Item(x, y, "coin", f"coin{num}.png")
                entities.add(item)
                items.append(item)
                num %= 4
                num += 1

            elif col == "k":
                item = Item(x, y, "keycard", "keycard.png")
                entities.add(item)
                items.append(item)

            elif col == "?":
                item = Item(x, y, "flip", "flip.png")
                entities.add(item)
                items.append(item)
            elif col == "p":
                hero = Player(x, y)
                left = right = run = False
                up = False
                entities.add(hero)

            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0

    total_level_width = len(level[0]) * PLATFORM_WIDTH
    total_level_height = len(level) * PLATFORM_HEIGHT
    return total_level_width, total_level_height, hero, run, right, left, up

# С О З Д А Н И Е  Ф О Н А  И  О К Н А  И Г Р Ы

pygame.init()
screen = pygame.display.set_mode(DISPLAY)
pygame.display.set_caption("while True")
bg = Surface((WIN_WIDTH, WIN_HEIGHT))
bg.fill(Color(BACKGROUND_COLOR))


# С О З Д А Н И Е  С Т Р О К И  С О С Т О Я Н И Я

info = pygame.Surface((1280, 30))
pygame.font.init()
info_font = pygame.font.Font(None, 40)

message = pygame.Surface((1280, 120))
message_font = pygame.font.SysFont("Comic Sans MS", 60, True)

# С О З Д А Н И Е  С П И С К О В  О Б Ъ Е К Т О В

entities = pygame.sprite.Group()
platforms = []
items = []
monsters = []
levels = [level, level2, level3]

# З А П О Л Н Е Н И Е  С П И С К О В  О Б Ъ Е К Т О В

timer = pygame.time.Clock()

total_level_width, total_level_height, hero, run, right, left, up = create_level(level)

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
pygame.mixer.music.load('Music/main_music.ogg')


# М е н ю

x_menu = WIN_WIDTH // 2 + 50
y_menu = WIN_HEIGHT // 2 - 100
start_punkts = [(x_menu, y_menu, u'Игра', (150,150,150), (50,250,50), 0),
              (x_menu, y_menu + 120, u'Выход', (150,150,150), (50,250,50), 1)]
start_menu = Menu(start_punkts)


while True:
    start_menu.menu()
    pygame.mixer.music.play(-1)
#О С Н О В Н О Й  И Г Р О В О Й  Ц И К Л

    camera = Camera(camera_configure, total_level_width, total_level_height)
    running = True
    num_of_level = 0
    while running:
        pygame.mixer.music.unpause()
        timer.tick(60)

        if hero.dead:
            pygame.mixer.music.stop()
            hero.sound_of_death.play()
            pygame.time.wait(4000)

            if hero.hp > 1:
                hero.hp -= 1
            else:

                total_level_width, total_level_height, hero, run, right, left, up = create_level(levels[0])
                camera = Camera(camera_configure, total_level_width, total_level_height)
                num_of_level = 0
            pygame.mixer.music.play()
            hero.respawn()

        elif hero.level_passed:
            num_of_level += 1
            pygame.mixer.music.stop()
            hero.sound_level_passed.play()
            pygame.time.wait(5200)
            if num_of_level != len(levels):

                total_level_width, total_level_height, hero, run, right, left, up = create_level(levels[num_of_level])
                camera = Camera(camera_configure, total_level_width, total_level_height)
                pygame.mixer.music.play()
            else:
                num_of_level = 0
                start_menu.menu()
                total_level_width, total_level_height, hero, run, right, left, up = create_level(levels[num_of_level])
                camera = Camera(camera_configure, total_level_width, total_level_height)
                pygame.mixer.music.play()

        for e in pygame.event.get():

            if e.type == pygame.QUIT:
                sys.exit()

            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                run = up = left = right = False
                pygame.mixer.music.pause()
                start_menu.menu(True)
            if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
                jump_time = pygame.time.get_ticks()

                hero.image = IMAGE_PLAYER_UP

            if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
                left = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
                right = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_LSHIFT:
                run = True

            if e.type == pygame.KEYUP and e.key == pygame.K_UP:

                ticks = (pygame.time.get_ticks() - jump_time) / 200 #200
                if ticks > 0.60:
                    ticks = 1
                if ticks < 0.5:
                    ticks = 0.5


                if ticks > 0:
                    hero.jump_mult = ticks
                    up = True

                    hero.sound_of_jump.play()

            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                right = False
            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                left = False
            if e.type == pygame.KEYUP and e.key == pygame.K_LSHIFT:
                run = False

        Draw_Game(hero.flip)