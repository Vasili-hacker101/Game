import pygame
from Player import *
from Blocks import *
from Items import *
from Levels import *

WIN_WIDTH = 1280
WIN_HEIGHT = 720
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "black"

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


def Draw_Game():
    global screen
    screen.blit(bg, (0, 0))

    for i in items:
        i.update(hero)

    camera.update(hero)
    hero.update(run, left, right, up, platforms + items)

    for e in entities:
        screen.blit(e.image, camera.apply(e))

    info.fill((0, 0, 0))
    info.set_colorkey((0, 0, 0))
    info_str = u"Счет: " + str(hero.num_of_coins)
    if hero.num_of_keycards > 0:
        info_str += ", Ключ!"
    info.blit(info_font.render(info_str, 1, (255, 255, 255)), (10, 5))
    flip_it = pygame.transform.flip(pygame.display.get_surface(), 0, 0)
    screen.blit(flip_it, (0, 0))
    screen.blit(info, (0, 0))
    pygame.display.update()

# С О З Д А Н И Е  Ф О Н А  И  О К Н А  И Г Р Ы

pygame.init()
screen = pygame.display.set_mode(DISPLAY)
pygame.display.set_caption("CoffeMan - T H E  G A M E")
bg = Surface((WIN_WIDTH, WIN_HEIGHT))
bg.fill(Color(BACKGROUND_COLOR))

# С О З Д А Н И Е  С Т Р О К И  С О С Т О Я Н И Я

info = pygame.Surface((1280, 30))
pygame.font.init()
info_font = pygame.font.Font(None, 40)

# С О З Д А Н И Е  О Б Ъ Е К Т А - И Г Р О К А

#hero = Player(55, 55)
#left = right = run = False
#up = False

# С О З Д А Н И Е  С П И С К О В  О Б Ъ Е К Т О В

entities = pygame.sprite.Group()
platforms = []
items = []

#entities.add(hero)

# З А П О Л Н Е Н И Е  С П И С К О В  О Б Ъ Е К Т О В

timer = pygame.time.Clock()
x = y = 0
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

        elif col == "|":
            door = Door(x, y)
            entities.add(door)
            platforms.append(door)

        elif col == "+":
            item = Item(x, y, "coin", "coin.png")
            entities.add(item)
            items.append(item)

        elif col == "k":
            item = Item(x, y, "keycard", "keycard.png")
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

#pygame.mixer.pre_init(44100, -16, 1, 512)
#pygame.mixer.init()
#sound = pygame.mixer.Sound('Music/main_music.ogg')
#sound.play(-1)


#О С Н О В Н О Й  И Г Р О В О Й  Ц И К Л

camera = Camera(camera_configure, total_level_width, total_level_height)
running = True

while running:
    timer.tick(60)

    if hero.dead:
        #sound.stop()
        #hero.sound_of_death.play()
        pygame.time.wait(4000)
        #sound.play()
        hero.respawn()

    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
            up = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
            left = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
            right = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_LSHIFT:
            run = True

        if e.type == pygame.KEYUP and e.key == pygame.K_UP:
            up = False
        if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
            right = False
        if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
            left = False
        if e.type == pygame.KEYUP and e.key == pygame.K_LSHIFT:
            run = False

    Draw_Game()