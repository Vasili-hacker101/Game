
from Player import *

from Functions import check_img

CELL_SIZE = 40
#ICON_DIR = os.path.dirname(__file__)


class Item(sprite.Sprite):

    def __init__(self, x, y, name, img):
        sprite.Sprite.__init__(self)
        self.draw(x, y, img)
        self.name = name

    def draw(self, x, y, fimg):
        self.image = Surface((CELL_SIZE, CELL_SIZE))
        self.rect = Rect(x, y, CELL_SIZE, CELL_SIZE)
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        self.image = check_img(f"./images/Items/{fimg}", 40)


#class Weapon(Item):
#    def __init__(self, dmg, mag, bull_speed, reload_speed):
#        self.dmg = dmg
#        self.mag = mag
#        self.bull_speed = bull_speed
#        self.reload_speed = reload_speed
#
#    def shoot(self, bullet):
#        bullet.shot(self.bull_speed)
#
#    def reload(self):
#        time.sleep(self.reload_speed)
