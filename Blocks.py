
from pygame import sprite, Surface, Color, Rect, image
import random
PLATFORM_WIDTH = 40
PLATFORM_HEIGHT = 40
PLATFORM_COLOR = "green"
АRROW_COLOR = "black"
FLAME_COLOR = "red"
SPEED_OF_FIREBALL = 5

IMAGE_UP = image.load("./images/Blocks/up/up.png")
#IMAGE_EXIT = image.load("./images/Blocks/exit.png")

FLAME_ANIM = [image.load("./images/Blocks/lava/lava1.png"),
              image.load("./images/Blocks/lava/lava2.png"),
              image.load("./images/Blocks/lava/lava3.png"),]

EXIT_ANIM = [image.load("./images/Blocks/exit/exit1.png"),
             image.load("./images/Blocks/exit/exit2.png"),
             image.load("./images/Blocks/exit/exit3.png"),
             image.load("./images/Blocks/exit/exit4.png")]
EXIT_CLOSED = image.load("./images/Blocks/exit/exit_closed.png")

RIGHT_ANIM = [image.load("./images/Blocks/right/right1.png"),
             image.load("./images/Blocks/right/right2.png"),
             image.load("./images/Blocks/right/right3.png")]

LEFT_ANIM = [image.load("./images/Blocks/left/left1.png"),
             image.load("./images/Blocks/left/left2.png"),
             image.load("./images/Blocks/left/left3.png")]



class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load("./images/Blocks/platform.png")
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class Flame(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.count = 0
        self.frame = random.randint(0, 2)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(FLAME_COLOR))
        self.image = FLAME_ANIM[0]

    def update(self):
        self.count += 1
        if self.count == 20:
            self.animate()
            self.count = 0

    def animate(self):
        if self.frame < len(FLAME_ANIM) - 1:
            self.frame += 1
        else:
            self.frame = 0
        self.image = FLAME_ANIM[self.frame]

class Right_Arrow(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color("black"))
        self.image = RIGHT_ANIM[0]
        self.frame = 0
        self.count = 0
    def update(self):
        self.count += 1
        if self.count == 20:
            self.animate()
            self.count = 0

    def animate(self):
        if self.frame < len(RIGHT_ANIM) - 1:
            self.frame += 1
        else:
            self.frame = 0
        self.image = RIGHT_ANIM[self.frame]


class Left_Arrow(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color("black"))
        self.image = LEFT_ANIM[0]
        self.frame = 0
        self.count = 0

    def update(self):
        self.count += 1
        if self.count == 20:
            self.animate()
            self.count = 0

    def animate(self):
        if self.frame < len(LEFT_ANIM) - 1:
            self.frame += 1
        else:
            self.frame = 0
        self.image = LEFT_ANIM[self.frame]

class Trampoline(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color("black"))
        self.image = IMAGE_UP


class Exit(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.count = 0
        self.frame = 0
        self.image.fill(Color("black"))
        self.image.set_colorkey((0, 0, 0))
        self.image = EXIT_CLOSED
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

    def update(self, hero):
        self.count += 1
        if self.count == 20:
            self.animate(hero)
            self.count = 0

    def animate(self, hero):
        if hero.num_of_keycards != 0:
            if self.frame < len(EXIT_ANIM) - 1:
                self.frame += 1
            else:
                self.frame = 0
            self.image = EXIT_ANIM[self.frame]

