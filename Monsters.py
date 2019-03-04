from pygame import sprite, image, Surface, Color, Rect
SPEED_OF_FIREBALL = 5
FIREBALL_SIZE = 20
FLAME_COLOR = "red"


class FireBall(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((FIREBALL_SIZE, FIREBALL_SIZE))
        self.image.fill(Color(FLAME_COLOR))
        self.x_speed = SPEED_OF_FIREBALL
        self.rect = Rect(x, y, FIREBALL_SIZE, FIREBALL_SIZE)

    def update(self, platforms):
        self.rect.x += self.x_speed
        self.collide(self.x_speed, platforms)

    def collide(self, x_speed, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):
                if x_speed > 0:
                    self.rect.right = p.rect.left

                if x_speed < 0:
                    self.rect.left = p.rect.right

                if self.rect.left == p.rect.right or self.rect.right == p.rect.left:
                    self.x_speed = -self.x_speed