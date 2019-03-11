import pygame
PLATFORM_WIDTH = 40
PLATFORM_HEIGHT = 40
PLATFORM_COLOR = "green"
АRROW_COLOR = "black"



IMAGE_UP = pygame.image.load("./images/Blocks/up/up.png")

FLAME_ANIM = [pygame.image.load("./images/Blocks/lava/lava1.png"),
              pygame.image.load("./images/Blocks/lava/lava2.png"),
              pygame.image.load("./images/Blocks/lava/lava3.png"),]

EXIT_ANIM = [pygame.image.load("./images/Blocks/exit/exit1.png"),
             pygame.image.load("./images/Blocks/exit/exit2.png"),
             pygame.image.load("./images/Blocks/exit/exit3.png"),
             pygame.image.load("./images/Blocks/exit/exit4.png")]
EXIT_CLOSED = pygame.image.load("./images/Blocks/exit/exit_closed.png")

RIGHT_ANIM = [pygame.image.load("./images/Blocks/right/right1.png"),
              pygame.image.load("./images/Blocks/right/right2.png"),
              pygame.image.load("./images/Blocks/right/right3.png")]

LEFT_ANIM = [pygame.image.load("./images/Blocks/left/left1.png"),
             pygame.image.load("./images/Blocks/left/left2.png"),
             pygame.image.load("./images/Blocks/left/left3.png")]


WIN_WIDTH = 1280
WIN_HEIGHT = 720
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "black"
BACKGROUND_IMAGE_MENU = pygame.image.load("./images/Background/Background.png")


MOVE_SPEED = 7
SPRINT_SPEED = 21
WIDTH = 40
HEIGHT = 40
COLOR = "blue"
JUMP_POWER = 10
GRAVITY = 0.25
CELL_SIZE = 40

IMAGE_PLAYER_STAY = pygame.image.load("./images/Player/hero.png")
IMAGE_PLAYER_RIGHT = pygame.image.load("./images/Player/hero_right2.png")
IMAGE_PLAYER_LEFT = pygame.image.load("./images/Player/hero_left2.png")
IMAGE_PLAYER_UP = pygame.image.load("./images/Player/hero_up2.png")
IMAGE_PLAYER_DIE = pygame.image.load("./images/Player/hero_die.png")

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()

SPEED_OF_FIREBALL = 5
FIREBALL_SIZE = 30
FLAME_COLOR = "red"

FIREBALL_ANIM = [pygame.image.load("./images/Enemys/enemy1.png"),
                 pygame.image.load("./images/Enemys/enemy2.png"),
                 pygame.image.load("./images/Enemys/enemy3.png"),]
