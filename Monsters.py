from pygame import sprite, image, Surface, Color, Rect
SPEED_OF_FIREBALL = 5
FIREBALL_SIZE = 30
FLAME_COLOR = "red"

FIREBALL_ANIM = [image.load("./images/Enemys/enemy1.png"),
                 image.load("./images/Enemys/enemy2.png"),
                 image.load("./images/Enemys/enemy3.png"),]

class FireBall(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((FIREBALL_SIZE, FIREBALL_SIZE))
        self.image = FIREBALL_ANIM[0]
        self.frame = 0
        self.count = 0
        self.x_speed = SPEED_OF_FIREBALL
        self.rect = Rect(x, y, FIREBALL_SIZE, FIREBALL_SIZE)

    def update(self, platforms):
        self.count += 1
        self.rect.x += self.x_speed
        if self.count == 2:
            self.animate()
            self.count = 0
        self.collide(self.x_speed, platforms)

    def animate(self):
        if self.frame < len(FIREBALL_ANIM) - 1:
            self.frame += 1
        else:
            self.frame = 0
        self.image = FIREBALL_ANIM[self.frame]

    def collide(self, x_speed, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):
                if x_speed > 0:
                    self.rect.right = p.rect.left

                if x_speed < 0:
                    self.rect.left = p.rect.right

                if self.rect.left == p.rect.right or self.rect.right == p.rect.left:
                    self.x_speed = -self.x_speed