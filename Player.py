
from pygame import mixer
from Blocks import *
from Items import *
from Monsters import *


MOVE_SPEED = 7
SPRINT_SPEED = 21
WIDTH = 40
HEIGHT = 40
COLOR = "blue"
JUMP_POWER = 10
GRAVITY = 0.25

IMAGE_PLAYER_STAY = image.load("./images/Player/hero.png")
IMAGE_PLAYER_RIGHT = image.load("./images/Player/hero_right2.png")
IMAGE_PLAYER_LEFT = image.load("./images/Player/hero_left2.png")
IMAGE_PLAYER_UP = image.load("./images/Player/hero_up2.png")
IMAGE_PLAYER_DIE = image.load("./images/Player/hero_die.png")

mixer.pre_init(44100, -16, 1, 512)
mixer.init()


class Player(sprite.Sprite):

    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.x_speed = 0
        self.y_speed = 0

        self.save_y = 0
        self.save_x = 0

        self.startX = x
        self.startY = y

        self.num_of_coins = 0
        self.num_of_keycards = 0
        self.onGround = False
        self.dead = False
        self.level_passed = False
        self.flip = False
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.image.set_colorkey((0, 0, 0))

        self.image_player_stay = image.load("./images/Player/hero.png")

        self.image = IMAGE_PLAYER_STAY

        self.frames = []

        self.rect = Rect(x, y, WIDTH, HEIGHT)

        self.sound_of_jump = mixer.Sound('Music/jump.ogg')
        self.sound_of_death = mixer.Sound('Music/game_over.ogg')
        self.sound_of_collecting_coins = mixer.Sound('Music/sound_of_coin.ogg')
        self.sound_level_passed = mixer.Sound('Music/level_passed.ogg')

    def update(self, run, left, right, up, platforms, monsters):

        if up:
            if self.onGround:
                self.y_speed = -JUMP_POWER
                self.image = IMAGE_PLAYER_UP
                self.sound_of_jump.play()

        if left:
            self.x_speed = -MOVE_SPEED

            if run:
                self.x_speed = -SPRINT_SPEED
            self.image = IMAGE_PLAYER_LEFT

        if right:
            self.x_speed = MOVE_SPEED

            if run:
                self.x_speed = SPRINT_SPEED

            self.image = IMAGE_PLAYER_RIGHT

        if not (left or right):
            self.x_speed = 0
            if not up:
                self.image = IMAGE_PLAYER_STAY

        if not self.onGround:
            self.y_speed += GRAVITY

        self.onGround = False
        self.rect.y += self.y_speed
        self.collide(0, self.y_speed, platforms, monsters)

        self.rect.x += self.x_speed
        self.collide(self.x_speed, 0, platforms, monsters)

    def die(self):
        self.dead = True
        self.image = IMAGE_PLAYER_DIE

    def respawn(self):
        self.dead = False
        self.image = IMAGE_PLAYER_STAY
        self.x_speed = 0
        self.y_speed = 0
        self.teleporting(self.startX, self.startY)

    def teleporting(self, goX, goY):
        self.rect.x = goX
        self.rect.y = goY

    def collide(self, x_speed, y_speed, platforms, monsters):
        for p in platforms:
            if sprite.collide_rect(self, p):

                if x_speed > 0:
                    self.save_x = self.x_speed
                    self.rect.right = p.rect.left



                if x_speed < 0:
                    self.save_x = self.x_speed
                    self.rect.left = p.rect.right

                if y_speed > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.save_y = self.y_speed
                    self.y_speed = 0

                if y_speed < 0:
                    self.rect.top = p.rect.bottom
                    self.save_y = self.y_speed
                    self.y_speed = 0

                if self.rect.bottom == p.rect.top:
                    if isinstance(p, Flame):
                        self.die()
                    elif isinstance(p, Right_Arrow):
                        self.x_speed += 5

                    elif isinstance(p, Left_Arrow):
                        self.x_speed -= 5

                    elif isinstance(p, Trampoline):
                        self.y_speed = -self.save_y * 1.25
                        self.sound_of_jump.play()

                if isinstance(p, Exit):
                    if self.num_of_keycards > 0:
                        self.level_passed = True

                elif isinstance(p, Item):
                    self.x_speed = self.save_x
                    self.y_speed = self.save_y
                    p.image.fill(Color("green"))
                    p.rect = Rect(0, 0, 0, 0)
                    if p.name == "coin":
                        self.num_of_coins += 1
                        self.sound_of_collecting_coins.play()
                    elif p.name == "keycard":
                        self.num_of_keycards += 1
                        self.sound_of_collecting_coins.play()
                    elif p.name == "flip":
                        self.flip = not self.flip

        for m in monsters:
            if sprite.collide_rect(self, m):
                if isinstance(m, FireBall):
                    self.die()

